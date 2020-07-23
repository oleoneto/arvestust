from rest_framework import serializers


class ArvestustRecordSerializerMixin(serializers.BaseSerializer):

    class Meta:
        exclude = (
            'uuid',
            'object_id',
            'content_type',
        )
