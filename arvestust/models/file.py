from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from .abstracts import ArvestustFile
from .comment import Comment
from .activity import Activity


class File(ArvestustFile):
    comments = GenericRelation(Comment, related_query_name='files')

    likes = GenericRelation(Activity, related_query_name='comments')
    votes = GenericRelation(Activity, related_query_name='comments')
    saves = GenericRelation(Activity, related_query_name='comments')
    reports = GenericRelation(Activity, related_query_name='comments')

    class Meta:
        db_table = 'arvestust_files'

    def get_absolute_url(self):
        return reverse('arvestust:file-detail', kwargs={'slug': self.slug})
