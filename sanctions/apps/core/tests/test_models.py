""" Tests for core models. """

from django.test import TestCase
from django_dynamic_fixture import G
from social_django.models import UserSocialAuth

from sanctions.apps.core.models import User


class UserTests(TestCase):
    """ User model tests. """
    TEST_CONTEXT = {'foo': 'bar', 'baz': None}

    def test_access_token(self):
        user = G(User)
        self.assertIsNone(user.access_token)

        social_auth = G(UserSocialAuth, user=user)
        self.assertIsNone(user.access_token)

        access_token = 'My voice is my passport. Verify me.'
        social_auth.extra_data['access_token'] = access_token
        social_auth.save()
        self.assertEqual(user.access_token, access_token)

    def test_string(self):
        """Verify that the model's string method returns the user's username."""
        username = 'Bob123'
        user = G(User, username=username)
        self.assertEqual(str(user), username)
