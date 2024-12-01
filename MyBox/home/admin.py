from django.contrib import admin
from .models import Comment, Rating

# Register your models here.
admin.site.register(Comment)
admin.site.register(Rating)