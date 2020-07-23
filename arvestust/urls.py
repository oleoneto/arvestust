# arvestust:urls
from django.urls import include, path
from .views.routes import routes

app_name = 'arvestust'

urlpatterns = [] + routes
