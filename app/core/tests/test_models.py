from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModels(TestCase):

    def test_create_user_with_email_and_password(self):
        email = 'test@londonappdevloper@gmail.com'
        password = 'testCase1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email = 'test@londonappdevloper@GMAIL.COM'
        password = 'test12234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
            )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')