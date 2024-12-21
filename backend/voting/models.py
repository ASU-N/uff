from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    party = models.CharField(max_length=255)
    imageUrl = models.URLField(default='http://default.url')  # Set a default value

    def __str__(self):
        return self.name


class Election(models.Model):
    deadline = models.DateTimeField()
    election_name = models.CharField(max_length=255)

    def __str__(self):
        return self.election_name

