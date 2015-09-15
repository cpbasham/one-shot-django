from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy # reverse causes circular import
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .utils import get_items
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
	return render(request, 'league_item_sets/edit.html', {'item_data': get_items(), 'item_set': itemset})



	# data = get_items()
	# s = ""
	# for key in data:
	# 	# return HttpResponse(str(data[key]))
	# 	s += key + ": " + str(data[key]) + "<br><br>-----------------------<br><br>"
	# return HttpResponse(s)