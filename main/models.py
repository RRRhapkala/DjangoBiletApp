from django.db import models
from django.contrib.auth.models import User

# SQLS.
class Event(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(null=True)
    address = models.CharField(max_length = 100)
    preview_image = models.CharField(max_length = 200)
    date = models.DateTimeField()
    price = models.SmallIntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    category = models.CharField(max_length = 8)
    users = models.ManyToManyField(User)