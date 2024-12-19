from django.db import models

# Create your models here.
from django.db import models

class Voter(models.Model):
    voter_id = models.CharField(max_length=100, unique=True)
    face_data = models.BinaryField()

    def __str__(self):
        return self.voter_id
