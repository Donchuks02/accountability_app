from django.shortcuts import render
from django.views.generic import TemplateView
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePageView(TemplateView):
  template_name = "home.html"


class DashboardView(LoginRequiredMixin,TemplateView):
      template_name = 'dashboard.html'

      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.filter(user=self.request.user)
        return context

