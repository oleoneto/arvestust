from rest_framework import serializers
from ..serializers import CommentSerializer
from ..models import File


class FileSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    class Meta:
        model = File
        exclude = (
            'uuid',
            'object_id',
            'content_type',
        )
