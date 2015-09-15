from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'(?P<itemset_pk>\d+)/edit$', views.edit, name="edit")
]
