from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .managers import ActivityManager
from .abstracts import ArvestustRecord


class Activity(ArvestustRecord):

    FAVORITE = 'FAVORITE'
    FOLLOW = 'FOLLOW'
    BOOKMARK = 'BOOKMARK'
    LIKE = 'LIKE'
    REPORT = 'REPORT'
    VOTE_DOWN = 'DOWN_VOTE'
    VOTE_UP = 'UP_VOTE'

    ACTIVITY_TYPES = (
        (BOOKMARK, 'Bookmark'),
        (FAVORITE, 'Favorite'),
        (FOLLOW, 'Follow'),
        (LIKE, 'Like'),
        (REPORT, 'Report'),
        (VOTE_DOWN, 'Down Vote'),
        (VOTE_UP, 'Up Vote'),
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    activity_type = models.CharField(
        max_length=15,
        choices=ACTIVITY_TYPES
    )

    class Meta:
        db_table = 'arvestust_activities'
        unique_together = ('object_id', 'user', 'content_type')

    objects = ActivityManager()

    def clean(self):
        super().clean()
        qs = Activity.objects.get_matches(
            pk=self.pk,
            user=self.user,
            obj_id=self.object_id,
        )
        if qs.count() > 0:
            raise ValidationError(_('User has already added this content.'))

    def get_absolute_url(self):
        return reverse('arvestust:activity-detail', kwargs={'slug': self.slug})
