from rest_framework import viewsets
from arvestust.viewsets.router import router
from arvestust.models import Like
from arvestust.serializers import LikeSerializer
from arvestust.viewsets.mixins import ArvestustRecordMixin


class LikeViewSet(ArvestustRecordMixin, viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.get_for_user(user=self.request.user)


router.register('likes', LikeViewSet)
