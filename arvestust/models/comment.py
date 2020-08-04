from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .managers import CommentManager
from .abstracts import ArvestustRecord
from .activity import Activity


class Comment(ArvestustRecord):
    user = models.ForeignKey(
        get_user_model(),
        related_name='comments',
        on_delete=models.DO_NOTHING,
        verbose_name=_('author')
    )
    content = models.TextField(blank=True, verbose_name=_('content'))

    likes = GenericRelation(Activity, related_query_name='comments')
    votes = GenericRelation(Activity, related_query_name='comments')
    saves = GenericRelation(Activity, related_query_name='comments')
    reports = GenericRelation(Activity, related_query_name='comments')

    def is_inappropriate(self):
        return self.reports.count() >= 5

    def has_likes(self):
        return self.likes.count() > 0

    class Meta:
        db_table = 'arvestust_comments'
        indexes = [models.Index(fields=['user', 'created_at'])]
        ordering = ['-created_at']

    objects = CommentManager()

    def get_absolute_url(self):
        return reverse('arvestust:comment-detail', kwargs={'slug': self.slug})
