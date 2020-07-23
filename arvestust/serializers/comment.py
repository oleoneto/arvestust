from rest_framework import serializers
from ..models import Comment
from .like import LikeSerializer


class CommentSerializer(serializers.ModelSerializer):

    likes = LikeSerializer(many=True, allow_null=True)

    class Meta:
        model = Comment
        exclude = (
            'uuid',
            'object_id',
            'content_type',
            'reports',
        )
