from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^items/?$', views.item_availability, name="item_availability"),
	url(r'^item_sets/(?P<itemset_pk>\d+)$', views.update_set, name="update_set"),
	url(r'^item_sets/(?P<itemset_pk>\d+)/item_categories/new$', views.new_row, name="new_row"),
	url(r'^item_categories/(?P<itemrow_pk>\d+)/items$', views.update_row, name="update_row"),
	url(r'^item_categories/(?P<itemrow_pk>\d+)$', views.delete_row, name="delete_row"),
	url(r'^items/(?P<item_pk>\d+)$', views.delete_item, name="delete_item"),
]
