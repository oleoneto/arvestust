from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .like import Like
from .managers import CommentManager
from .abstracts import ArvestustRecord


class Comment(ArvestustRecord):
    user = models.ForeignKey(
        get_user_model(),
        related_name='comments',
        on_delete=models.DO_NOTHING,
        verbose_name=_('author')
    )
    content = models.TextField(blank=True, verbose_name=_('content'))
    likes = GenericRelation(Like, related_query_name='comments')
    reports = models.ManyToManyField(
        get_user_model(),
        related_name='reported_comments',
        verbose_name=_('reports'),
        blank=True
    )

    @property
    def is_inappropriate(self):
        return self.reports.count() >= 5

    @property
    def has_likes(self):
        return self.likes.count() > 0

    class Meta:
        db_table = 'arvestust_comments'
        indexes = [models.Index(fields=['user', 'created_at'])]
        ordering = ['-created_at']

    objects = CommentManager()

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'slug': self.slug})
