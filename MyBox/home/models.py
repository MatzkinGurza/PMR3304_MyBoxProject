from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from store.models import Box

class Comment(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return '%s - %s' %(self.box.name, self.name)
    
    def get_absolute_url(self):
        return reverse('home:box-details', args=[str(self.box.pk)])
    
class Rating(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    ip = models.CharField(max_length=20,blank=True)
    status= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s by %s' %(self.box, self.rating, self.user)