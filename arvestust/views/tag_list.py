from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .urls import urlpatterns
from ..models import Tag


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tag_list.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


urlpatterns.append(
    path('tags/', TagListView.as_view(), name='tag-list')
)
