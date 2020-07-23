# arvestust:routes

"""
Import routes into each view module and append the path to the list:
# lua/file_cabinet/views.my_view.py
from django.urls import path
from lua.file_cabinet.views.routes import routes

def my_view(request):
    ...

routes.append(
    path('', my_view, name='my-view')
)


Append the whole list to your urlpatterns:
# lua/file_cabinet/urls.py
from lua.file_cabinet.views.routes import routes

urlpatterns = [
    ...
] + routes
"""

routes = []
