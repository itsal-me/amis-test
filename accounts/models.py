from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('ADMIN', 'Admin'),
        ('FARMER', 'Farmer'),
        ('BUYER', 'Buyer'),
        ('SELLER', 'Seller'),
        ('ANALYST', 'Market Analyst'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    
    def __str__(self):
        return f"{self.username} - {self.user_type}"