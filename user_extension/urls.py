from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^login/?$', views.login, name='login'),
	url(r'^logout/?$', views.logout, name='logout'),
	url(r'^register/?$', views.register, name='register'),
	url(r'^itemsets/', include('league_item_sets.urls', namespace='itemsets')),
]