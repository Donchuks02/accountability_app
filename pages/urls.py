from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view() , name="home"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard")
]