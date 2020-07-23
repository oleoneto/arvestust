# arvestust:api
from django.urls import include, path
from .viewsets.router import router

app_name = 'arvestust'

urlpatterns = [
   path('', include(router.urls)),
]
