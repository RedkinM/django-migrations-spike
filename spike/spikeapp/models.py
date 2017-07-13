from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
