from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy # reverse causes circular import
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .utils import get_items, ITEM_SPRITE_HEAD
from .models import *

# Create your views here.
@login_required(login_url=reverse_lazy("user:login"))
def index(request):
	return render(request, 'league_item_sets/index.html', {"user": request.user, "item_sets": request.user.itemset_set.all()})

@login_required(login_url=reverse_lazy("user:login"))
def edit(request, itemset_pk):
	itemset = get_object_or_404(ItemSet, pk=itemset_pk)
	if itemset.creator_id != request.user.id:
		return redirect(reverse_lazy("user:itemsets:index"))

	item_data = get_items()

	setdata = {}
	setdata["id"] = itemset.id
	setdata["name"] = itemset.name
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

	return render(request, 'league_item_sets/edit.html', {'item_data': item_data, 'item_set_data': setdata, 'ITEM_SPRITE_HEAD': ITEM_SPRITE_HEAD})



	# data = get_items()
	# s = ""
	# for key in data:
	# 	# return HttpResponse(str(data[key]))
	# 	s += key + ": " + str(data[key]) + "<br><br>-----------------------<br><br>"
	# return HttpResponse(s)