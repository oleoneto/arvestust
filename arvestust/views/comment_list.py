from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.urls import path
from django.contrib.auth.mixins import LoginRequiredMixin
from .urls import urlpatterns
from ..models import Comment
from ..forms import CommentForm


class CommentListView(LoginRequiredMixin, ListView, CreateView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'comment_list.html'
    form_class = CommentForm
    paginate_by = 50

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


urlpatterns.append(
    path('comments/', CommentListView.as_view(), name='comment-list')
)
