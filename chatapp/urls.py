from django.urls import path
from .views import CreateRoom, MessageView

urlpatterns = [
    path('', CreateRoom, name='create_room'),
    path('<str:room_name>/<str:username>/', MessageView, name='room'),
]
