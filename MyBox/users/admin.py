from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'store_address', 'store_name', 'join_date')  # Replaced 'location' with 'store_address'
    list_filter = ('user_type', 'join_date')
    search_fields = ('user__username', 'store_name')
