from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .utils import get_items

# Create your views here.
@login_required(login_url=reverse_lazy("user:login")) # reverse causes circular import
def index(request):
	return render(request, 'league_item_sets/index.html', {"user": request.user, "item_sets": request.user.itemset_set.all()})



	# data = get_items()
	# s = ""
	# for key in data:
	# 	# return HttpResponse(str(data[key]))
	# 	s += key + ": " + str(data[key]) + "<br><br>-----------------------<br><br>"
	# return HttpResponse(s)