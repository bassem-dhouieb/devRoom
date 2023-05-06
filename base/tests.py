import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Room, User
from .api.serializers import RoomSerializer
from .api import views

# initialize the APIClient app
client = Client()

class GetRoomTest(TestCase):
    def setUp(self):
        user = User.objects.create(
                name = 'Moula L\'informatique', email = 'hacker@fsociety.us')
        Room.objects.create(
                name='DevOps', host = user)
    def testGetRoom(self):
        room = Room.objects.get(name='DevOps')
        response = client.get(reverse(views.getRoom, args=[room.pk]))
        serializer = RoomSerializer(room, many=False)
        self.assertEqual(response.json(), serializer.data)

class GetAllRoomsTest(TestCase):
    def setUp(self):
        user = User.objects.create(
                name = 'Moula L\'informatique', email = 'hacker@fsociety.us')
        Room.objects.create(
                name='DevOps', host = user)
        Room.objects.create(
                name='Cloud', host = user)
        Room.objects.create(
                name='Artificial Intelligence', host = user)
        Room.objects.create(
                name='Mobile', host = user)
    def testGetAllRooms(self):
        rooms = Room.objects.all()
        response = client.get(reverse(views.getRooms))
        serializer = RoomSerializer(rooms, many=True)
        self.assertEqual(response.json(), serializer.data)
