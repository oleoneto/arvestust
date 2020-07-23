from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .routes import routes
from ..models import Like


class LikeListView(LoginRequiredMixin, ListView):
    model = Like
    context_object_name = 'likes'
    template_name = 'like_list.html'
    paginate_by = 50

    def get_queryset(self):
        return Like.objects.filter(
            author=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


routes.append(
    path('likes/', LikeListView.as_view(), name='like-list')
)
