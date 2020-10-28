from django.db import models

from django.db import models
from django.utils import timezone
import datetime

class My_travels_plan(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    def __str__(self):
        return self.title
    
    
class Places_visited(models.Model):
    city_name =  models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    date = models.DateField()
    my_travels_plan = models.ForeignKey(My_travels_plan, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.city_name
    
    
class Trip_Details(models.Model):
    Places_visited = models.ForeignKey(Places_visited, on_delete=models.CASCADE)
    links = models.URLField()
    title_trip = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title_trip      