from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your tests here.

class SignUpViewTests(TestCase):

    def test_signup_url_accessible(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.get(reverse('signup'))
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_signup_form_valid_data(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        self.assertRedirects(response, reverse('login'))  # Successful signup redirects to login
        self.assertEqual(User.objects.count(), 1)  # Ensure a user is created
        self.assertEqual(User.objects.first().username, 'newuser')  # Ensure correct username

    def test_signup_form_invalid_data(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'differentpassword',
        })
        self.assertEqual(response.status_code, 200)  # Form reloaded due to errors
        self.assertEqual(User.objects.count(), 0)  # Ensure no user is created

    def test_signup_existing_username(self):
        User.objects.create_user(username='existinguser', password='password123')
        response = self.client.post(reverse('signup'), {
            'username': 'existinguser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        self.assertEqual(response.status_code, 200)  # Form reloaded due to errors
        self.assertEqual(User.objects.count(), 1)  # Ensure no additional user is created
