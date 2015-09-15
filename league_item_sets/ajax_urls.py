from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^items/?$', views.item_availability, name="item_availability"),
	url(r'^item_sets/(?P<itemset_pk>\d+)?$', views.update, name="update_set"),
]
