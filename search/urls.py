from django.conf.urls import url, include
from . import views

#urlpattern is trimed till /search/ via /moviemanager/urls.py; then sent over here
urlpatterns = [
	url(r'^$',views.home),
	url(r'^[0-9]*',views.details)
]
