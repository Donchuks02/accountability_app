from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import FormView, DeleteView
from .models import Profile, FormModel
from .forms import ProfileForm, DailyCodingForm
from django.utils import timezone
from datetime import timedelta

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'create_profile.html'
    # Redirect to the dashboard after success
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileDeleteView(DeleteView):
        model = Profile
        template_name = 'profile_confirm_delete.html'
        success_url = reverse_lazy('dashboard')

class DailyCodingView(FormView):
    form_class = DailyCodingForm
    template_name = 'daily_coding_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(id=self.kwargs['profile_id'])
        if profile.last_submission and timezone.now() - profile.last_submission < timedelta(hours=24):
            context['form'] = None
        context['profile'] = profile
        return context

    def form_valid(self, form):
        profile = Profile.objects.get(id=self.kwargs['profile_id'])
        answer = "Yes" if form.cleaned_data['coded_today'] else "No"

        # Save the form response to FormModel
        FormModel.objects.create(user=self.request.user, question="Did you code for at least 2 hours today?", answer=answer)

        # If the answer is "Yes", update progress
        if form.cleaned_data['coded_today']:
            profile.progress += 3.3
            profile.last_submission = timezone.now()
            if profile.progress >= 99:
                profile.progress = 100
                profile.completed = True
            profile.save()
        else:
            # Just update the last submission time without changing progress
            profile.last_submission = timezone.now()
            profile.save()

        return super().form_valid(form)







