from rest_framework import viewsets
from rest_framework import permissions
from arvestust.viewsets.router import router
from arvestust.models import File
from arvestust.serializers import FileSerializer
from arvestust.viewsets.mixins import ArvestustFileMixin


class FileViewSet(ArvestustFileMixin, viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


router.register('files', FileViewSet)
