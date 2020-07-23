from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .routes import routes
from ..models import Follow


class FollowListView(LoginRequiredMixin, ListView):
    model = Follow
    context_object_name = 'follows'
    template_name = 'follow_list.html'
    paginate_by = 50

    def get_queryset(self):
        return Follow.objects.filter(
            author=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


routes.append(
    path('follows/', FollowListView.as_view(), name='follow-list')
)
