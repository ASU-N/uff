from django.urls import path
from .views import ElectionCountdownView, CandidateListView

urlpatterns = [
    path('api/election/countdown/', ElectionCountdownView.as_view(), name='election-countdown'),
    path('api/candidates/', CandidateListView.as_view(), name='candidate-list'),
]

