from rest_framework import viewsets
from rest_framework import permissions
from .router import router
from ..models import Tag
from ..serializers import TagSerializer
from .mixins import ArvestustRecordMixin


class TagViewSet(ArvestustRecordMixin, viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


router.register('tags', TagViewSet)
