from django.urls import path
from chat import views

urlpatterns = [
    path("chat/", views.ChatListView.as_view()),
    path("chat-messages/<int:pk>/", views.ChatMessagesListView.as_view())

]
