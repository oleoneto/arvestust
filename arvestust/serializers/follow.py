from rest_framework import serializers
from ..models import Follow


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        exclude = (
            'uuid',
            'object_id',
            'content_type',
        )
