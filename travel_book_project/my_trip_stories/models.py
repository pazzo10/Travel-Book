from django.db import models

from django.db import models
from django.utils import timezone
import datetime

class My_travels_plan(models.Model):
    trip_title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.trip_title
    
    
class Places_visited(models.Model):
    city_name =  models.CharField(max_length=100)
    start_date =  models.DateTimeField('date to go on trip')
    end_date = models.DateTimeField('date I ended the trip')
    links_sharing = models.URLField(max_length= 500)
    summury = models.TextField(blank=True)
    my_travels_plan = models.ForeignKey(My_travels_plan, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.city_name