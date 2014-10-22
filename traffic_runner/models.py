from django.db import models
from api_manager.models import Query

class TestPlan(models.Model):
    name = models.CharField(max_length=64)
    query = models.ForeignKey(Query)
    test_time = models.FloatField()
    interval = models.PositiveSmallIntegerField()
    started = models.DateTimeField(auto_now_add=True)
