from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

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

    def test_new_user_email_normalized(self):
        """test if user email is normalized"""
        email = 'deNeme@GmAiL.CoM'
        normalized = 'deneme@gmail.com'

        user = get_user_model().objects.create_user(
            email=email,
            password=None
        )

        self.assertEqual(user.email, normalized)

    def test_new_user_invalid_email(self):
        """test creaing with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='asdads')

    def test_create_new_super_user(self):
        """test creating super user"""
        user = get_user_model().objects.create_superuser(
                email='asdasd@asdasd.com',
                password='adsasda'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
