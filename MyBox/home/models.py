from django.contrib.auth.models import User
from django.db import models

class Box(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona a Box a um vendedor
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='boxes/', blank=True, null=True)  # Campo para upload da imagem

    def __str__(self):
        return self.name
