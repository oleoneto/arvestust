from rest_framework import viewsets
from rest_framework import permissions
from arvestust.viewsets.router import router
from arvestust.models import Comment
from arvestust.serializers import CommentSerializer
from arvestust.viewsets.mixins import ArvestustRecordMixin


class CommentViewSet(ArvestustRecordMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Comment.objects.get_for_user(
                user=self.request.user
            )
        return self.queryset


router.register('comments', CommentViewSet)
