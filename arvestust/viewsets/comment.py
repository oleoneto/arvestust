from rest_framework import viewsets
from arvestust.viewsets.router import router
from arvestust.models import Comment
from arvestust.serializers import CommentSerializer
from arvestust.viewsets.mixins import ArvestustRecordMixin


class CommentViewSet(ArvestustRecordMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.get_for_user(
            user=self.request.user
        )


# router.register('comments', CommentViewSet)
