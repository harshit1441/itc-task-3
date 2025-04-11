from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.id}: {self.title}"
