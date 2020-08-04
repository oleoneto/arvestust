from .record import ArvestustRecord
from ..managers.user_record import UserRecordManager


class UserRecord(ArvestustRecord):
    user = models.ForeignKey(
        get_user_model(),
        related_name='%(class)s',
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )

    class Meta:
        abstract = True
        unique_together = ('object_id', 'user',)
        indexes = [models.Index(fields=['user', 'created_at', 'object_id'])]

    objects = UserRecordManager()
