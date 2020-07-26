from rest_framework import serializers
from ..models import File
from ..serializers import LikeSerializer
from ..serializers import CommentSerializer


class FileSerializer(serializers.ModelSerializer):

    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = File
        exclude = (
            'uuid',
            'object_id',
            'content_type',
        )
