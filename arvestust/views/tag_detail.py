from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .urls import urlpatterns
from ..models import Tag


class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'tag_detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


urlpatterns.append(
    path('tags/<slug:slug>', TagDetailView.as_view(), name='tag-detail')
)
