from rest_framework import serializers
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = (
            'uuid',
            'object_id',
            'content_type',
            'reports',
        )
