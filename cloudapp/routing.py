from django.urls import path

from .consumer import WsConsumer

ws_urlpatterns = [
    path('ws/some_url/', WsConsumer.as_asgi()),
]
