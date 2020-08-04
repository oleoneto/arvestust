from django.utils import timezone
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from ..models import Comment
from .urls import urlpatterns


class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'comment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


urlpatterns.append(
    path('comments/<slug:slug>', CommentDetailView.as_view(), name='comment-detail')
)
