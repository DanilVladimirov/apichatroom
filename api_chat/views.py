from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatapp.models import Message
from api_chat.serializers import MessageSerializer
from django.core.paginator import Paginator, EmptyPage


@api_view(['GET'])
def get_page_of_messages(request, page):
    try:
        paginator = Paginator(list(Message.objects.all()), 10)
        messages = paginator.page(int(page)).object_list
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    except EmptyPage as err:
        return Response(str(err), status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status.HTTP_200_OK)
    except Message.DoesNotExist as err:
        return Response(str(err), status=status.HTTP_404_NOT_FOUND)
