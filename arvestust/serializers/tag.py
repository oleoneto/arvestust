from rest_framework import serializers
from ..models import Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        exclude = (
            'uuid',
            'object_id',
            'content_type',
        )
