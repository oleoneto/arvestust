from rest_framework import serializers
from ..models import Save


class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Save
        exclude = (
            'uuid',
            'object_id',
            'content_type',
        )
