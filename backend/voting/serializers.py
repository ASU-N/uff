from rest_framework import serializers
from .models import Candidate, Election

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'party', 'imageUrl']


class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ['id', 'election_name', 'deadline']

