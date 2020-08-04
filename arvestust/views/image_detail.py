from django.views.generic import DetailView
from django.urls import path
from .urls import urlpatterns
from ..models import Image


class ImageDetailView(DetailView):
    model = Image
    context_object_name = 'image'
    template_name = 'image_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


urlpatterns.append(
    path('images/<slug:slug>', ImageDetailView.as_view(), name='image-detail')
)
