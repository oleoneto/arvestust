from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .urls import urlpatterns
from ..models import File


class FileListView(LoginRequiredMixin, ListView):
    model = File
    context_object_name = 'files'
    template_name = 'file_list.html'
    paginate_by = 20

    def get_queryset(self):
        return File.objects.filter(
            uploaded_by=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


urlpatterns.append(
    path('files/', FileListView.as_view(), name='file-list')
)
