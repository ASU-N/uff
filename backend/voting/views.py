from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Candidate, Election
from .serializers import CandidateSerializer, ElectionSerializer
import datetime

def home(request):
    return render(request, 'home.html')

class ElectionCountdownView(APIView):
    def get(self, request):
        # Define the deadline for the election countdown
        deadline = datetime.datetime(2025, 1, 1)  
        now = datetime.datetime.now()
        remaining_time = deadline - now

        hours = remaining_time.days * 24 + remaining_time.seconds // 3600
        minutes = (remaining_time.seconds % 3600) // 60
        seconds = remaining_time.seconds % 60

        return JsonResponse({
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        })

class CandidateListView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch all candidates from the database
        candidates = Candidate.objects.all()
        # Serialize the candidates list
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

