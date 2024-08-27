from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'bio', 'currently_learning', 'github_profile_address']



# class DailyCodingForm(forms.Form):
#     coded_today = forms.BooleanField(label="Did you code or learn anything about coding for at least 2 hours today? if YES click on the checkbox and submit , if NO don't click on the checkbox just submit ", required=False)


class DailyCodingForm(forms.Form):
    coded_today = forms.BooleanField(
        label="Did you code or learn anything about coding for at least 2 hours today?",
        required=False
    )
    coding_notes = forms.CharField(
        label="What did you work on today?",
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        coded_today = cleaned_data.get("coded_today")
        coding_notes = cleaned_data.get("coding_notes")

        if coded_today and not coding_notes:
            self.add_error('coding_notes', "Please provide some notes on what you worked on today.")
