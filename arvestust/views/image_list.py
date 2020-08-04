from django.views.generic import ListView
from django.urls import path
from .urls import urlpatterns
from ..models import Image


class ImageListView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'image_list.html'
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


urlpatterns.append(
    path('images/', ImageListView.as_view(), name='image-list')
)
