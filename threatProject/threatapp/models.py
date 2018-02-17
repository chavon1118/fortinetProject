from django.db import models

class Threat(models.Model):
    date = models.DateTimeField('record date')
    filename = models.CharField(max_length=128)
    action = models.CharField(max_length=128)
    submit_type = models.CharField(max_length=128)
    rating = models.CharField(max_length=128)
			
    def __str__(self):
        return self.filename
