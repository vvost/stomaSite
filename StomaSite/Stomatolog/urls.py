from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "Stomatolog"

urlpatterns = [
	path("", views.HomeView.as_view(), name="home"),
]
