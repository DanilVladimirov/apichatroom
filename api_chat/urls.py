from django.urls import path
from api_chat.views import get_page_of_messages, create_message, get_message

urlpatterns = [
    path('messages/list/<int:page>/', get_page_of_messages, name='get_messages_page'),
    path('messages/create/', create_message, name='create_message'),
    path('messages/get/<int:message_id>/', get_message, name='get_message')
]
