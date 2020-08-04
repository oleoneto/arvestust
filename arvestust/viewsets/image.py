from rest_framework import viewsets
from rest_framework import permissions
from .router import router
from ..models import Image
from ..serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


router.register('images', ImageViewSet)
