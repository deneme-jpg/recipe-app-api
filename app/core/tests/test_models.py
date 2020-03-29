from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is sucessful"""
        email = 'mertmert@gmail.com'
        password = 'deNS!3neme123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def new_user_email_normalized(self):
        """test if user email is normalized"""
        email = 'deNeme@GmAiL.CoM'
        normalized = 'deNeme@gmail.com'

        user = get_user_model().objects.create_user(
            email=email,
            password='password12!'
        )

        self.assertEqual(user.email, normalized)
