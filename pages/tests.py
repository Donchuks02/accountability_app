from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase

# Create your tests here.

class HomePageTests(SimpleTestCase):

  def test_homepageview_url_exists_at_correct_location(self):
    response = self.client.get("/")
    self.assertEqual(response.status_code, 200)

  def test_homepage_view(self):
    response = self.client.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "home.html")
    self.assertContains(response, "Home")




class LoginViewTests(TestCase):

    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'secret'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_successful(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, '/dashboard/')  # Assuming successful login redirects to home

    def test_login_unsuccessful(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)


    # def test_authenticated_user_redirect(self):
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.get(reverse('login'))
    #     self.assertRedirects(response, '/dashboard/')

