from rest_framework import viewsets
from rest_framework import permissions
from .router import router
from ..models import Follow
from ..serializers import FollowSerializer
from ..viewsets.mixins import ArvestustRecordMixin


class FollowViewSet(ArvestustRecordMixin, viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def get_queryset(self):
        return Follow.objects.get_for_user(user=self.request.user)


router.register('follows', FollowViewSet)
