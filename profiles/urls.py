from django.urls import path
from . import views

urlpatterns = [
    path('create-profile/', views.ProfileCreateView.as_view(), name='create_profile'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
    path('profile/<int:profile_id>/daily-coding/', views.DailyCodingView.as_view(), name='daily_coding'),
]

# was about to create a delete profile view




