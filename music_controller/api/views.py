from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room
from .serializers import RoomSerializer


def main(request):
    return HttpResponse('TEST')


@api_view(['GET'])
def getRoom(request, code):
    room = Room.objects.get(code=code)
    serialized_room = RoomSerializer(room, many=False)
    return Response(serialized_room.data)


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
