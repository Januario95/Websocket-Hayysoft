from django.urls import path

from .views import index

app_name = 'cloudapp'


urlpatterns = [
    path('', index, name='index'),
]
