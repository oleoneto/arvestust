from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from .abstracts import ArvestustFile
from .like import Like
from .comment import Comment


class File(ArvestustFile):
    likes = GenericRelation(Like, related_query_name='files')
    comments = GenericRelation(Comment, related_query_name='files')

    class Meta:
        db_table = 'arvestust_files'

    def get_absolute_url(self):
        return reverse('file-detail', kwargs={'slug': self.slug})
