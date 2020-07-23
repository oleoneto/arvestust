from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .routes import routes
from ..models import Save


class SaveListView(LoginRequiredMixin, ListView):
    model = Save
    context_object_name = 'saves'
    template_name = 'save_list.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


routes.append(
    path('saves/', SaveListView.as_view(), name='save-list')
)
