from django.conf.urls import url
from . import views           


urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register), 
	url(r'^user$', views.user_profile),
	url(r'^create$', views.create), 
	url(r'^add$', views.add),
]
