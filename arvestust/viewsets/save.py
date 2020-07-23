from rest_framework import viewsets
from rest_framework import permissions
from .router import router
from ..models import Save
from ..serializers import SaveSerializer
from ..viewsets.mixins import ArvestustRecordMixin


class SaveViewSet(ArvestustRecordMixin, viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer

    def get_queryset(self):
        return Save.objects.get_for_user(user=self.request.user)


router.register('saves', SaveViewSet)
