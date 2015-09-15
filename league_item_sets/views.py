from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy # reverse causes circular import
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .utils import get_items, ITEM_SPRITE_HEAD, get_item_availability
import json
from .models import *

# Create your views here.
@login_required(login_url=reverse_lazy("user:login"))
def index(request):
	return render(request, 'league_item_sets/index.html', {"user": request.user, "item_sets": request.user.itemset_set.all(), "edit": False, "profile": True,})

@login_required(login_url=reverse_lazy("user:login"))
def edit(request, itemset_pk):
	itemset = get_object_or_404(ItemSet, pk=itemset_pk)
	if itemset.creator_id != request.user.id:
		return redirect(reverse_lazy("user:itemsets:index"))

	item_data = get_items()

	setdata = {}
	setdata["id"] = itemset.id
	setdata["name"] = itemset.name
	setdata["map"] = itemset.map
	setdata["game_type"] = itemset.game_type
	setdata["rows"] = []
	for row in itemset.itemrow_set.all():
		rowdata = {}
		rowdata["id"] = row.id
		rowdata["name"] = row.name
		rowdata["items"] = []
		for item in row.item_set.all():
			itemdata = {}
			itemdata["id"] = item.id
			itemdata["api_id"] = item.api_id
			itemdata["data"] = item_data[str(item.api_id)]
			rowdata["items"].append(itemdata)
		setdata["rows"].append(rowdata)

	return render(request, 'league_item_sets/edit.html', {'item_data': item_data, 'item_set_data': setdata, 'ITEM_SPRITE_HEAD': ITEM_SPRITE_HEAD, "edit": True, "profile": False,})

def item_availability(request):
	if request.is_ajax() == False:
		return redirect("/")
	else:
		return JsonResponse(get_item_availability())

# AJAX
def update_set(request, itemset_pk):
	if request.method == "GET":
		return redirect("/")
	elif request.method == "POST":
		item_set = ItemSet.objects.get(pk=itemset_pk)
		item_set.map = request.POST.get("map", item_set.map)
		item_set.game_type = request.POST.get("game-type", item_set.game_type)
		item_set.name = request.POST.get("name", item_set.name)
		item_set.save()
		return HttpResponse()
	elif request.method == "DELETE":
		item_set = ItemSet.objects.get(pk=itemset_pk)
		item_set.delete()
		return HttpResponse()

# AJAX
def update_row(request, itemrow_pk):
	if request.method == "GET":
		return redirect("/")
	elif request.method == "POST":
		item_row = ItemRow.objects.get(pk=itemrow_pk)
		item = Item.objects.create(api_id=request.POST.get("item_id"), parent_row=item_row)
		return JsonResponse({'id': item.id})

def new_row(request, itemset_pk):
	if request.method == "GET":
		if request.is_ajax():
			item_set = ItemSet.objects.get(pk=itemset_pk)
			row = ItemRow.objects.create(parent_set=item_set)
			return render(request, 'league_item_sets/_new_row.html', {'id': row.id})

def delete_row(request, itemrow_pk):
	if request.method == "GET":
		return redirect("/")
	elif request.method == "POST":
		row = ItemRow.objects.get(pk=itemrow_pk)
		row.name = request.POST.get("name", row.name)
		row.save()
		return HttpResponse()
	elif request.method == "DELETE":
		row = ItemRow.objects.get(pk=itemrow_pk)
		row.item_set.all().delete()
		row.delete()
		return HttpResponse()


def delete_item(request, item_pk):
	if request.method == "GET":
		return redirect("/")
	elif request.method == "DELETE":
		item = Item.objects.get(pk=item_pk)
		item.delete()
		return HttpResponse()


@login_required(login_url=reverse_lazy("user:login"))
def new_item_set(request):
	if request.method == "GET":
		item_set = ItemSet.objects.create(creator=request.user)
		return redirect(reverse_lazy("user:itemsets:edit_set", kwargs={'itemset_pk': item_set.pk}))
