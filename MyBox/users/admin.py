from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'store_name', 'join_date')
    list_filter = ('user_type', 'join_date')
    search_fields = ('user__username', 'store_name')
