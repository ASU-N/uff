from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Voter
from .serializers import VoterSerializer

def home(request):
    return HttpResponse("Welcome to the Online Voting System!")

@api_view(['POST'])
def login(request):
    voter_id = request.data.get('voter_id')
    face_data = request.data.get('face_data')  # Retrieve face data
    try:
        voter = Voter.objects.get(voter_id=voter_id)
        if voter.face_data == face_data:
            serializer = VoterSerializer(voter)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid face data.'}, status=status.HTTP_400_BAD_REQUEST)
    except Voter.DoesNotExist:
        return Response({'error': 'Voter not detected. Please register.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def register(request):
    voter_id = request.data.get('voter_id')
    face_data = request.data.get('face_data')
    voter_data = {'voter_id': voter_id, 'face_data': face_data}

    serializer = VoterSerializer(data=voter_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
