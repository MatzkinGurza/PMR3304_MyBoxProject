from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=[("seller", "Vendedor"), ("buyer", "Comprador")], default="buyer")

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"
