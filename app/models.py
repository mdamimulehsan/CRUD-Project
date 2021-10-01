from django.db import models


# Create your models here.
class Cricketers(models.Model):
    name = models.CharField(max_length=20, null=False)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name
