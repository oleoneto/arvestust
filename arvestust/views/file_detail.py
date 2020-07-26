from django.utils import timezone
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .routes import routes
from ..models import File
from ..forms import FileForm


class FileDetailView(LoginRequiredMixin, DetailView):
    model = File
    context_object_name = 'file'
    template_name = 'file_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


routes.append(
    path('files/<slug:slug>', FileDetailView.as_view(), name='file-detail')
)
