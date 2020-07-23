from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from ..comment import Comment


class CommentTestCase(APITestCase):

    # The client used to connect to the API
    client = APIClient()

    def setUp(self):
        """
        Prepare database and client.
        """

        # API endpoint
        self.namespace = '/v1/comments'

    @classmethod
    def setUpTestData(cls):
        # Create users
        cls.alice = get_user_model().objects.create(username="alice", email="alice@example.org")
        cls.bob = get_user_model().objects.create(username="bob", email="bob@example.org")

        # Create comments
        # cls.comment1 = Comment.objects.create(...)
        # cls.comment2 = Comment.objects.create(...)
        # cls.comment3 = Comment.objects.create(...)

    #################################################################
    # Require authentication
    def test_must_authenticate_to_read_comments(self):
        res = self.client.get(self.namespace)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_must_authenticate_to_create_comments(self):
        res = self.client.post(self.namespace)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    #################################################################
    # Allowed requests
    def test_create_comment(self):
        self.client.force_authenticate(user=self.alice)

        res = self.client.post(self.namespace, data={})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list_comment(self):
        self.client.force_authenticate(user=self.alice)

        res = self.client.get(self.namespace)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_comment(self):
        self.client.force_authenticate(user=self.alice)

        url = self.namespace + '/1'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        self.client.force_authenticate(user=self.alice)

        url = self.namespace + '/1'
        res = self.client.patch(url, data={})
        self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)

    def test_delete_comment(self):
        self.client.force_authenticate(user=self.alice)

        url = self.namespace + '/1'
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
