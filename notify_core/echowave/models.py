from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class UserModel(AbstractUser): # Keep It Simple and Stupid(KISS) for this simple project
    uuid = models.CharField(max_length=255, unique=True, default=uuid4, editable=False) 

    def __str__(self):
        return f"{self.pk}-{self.username}"
    

class NotifyTypeModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Notify Types"

    def __str__(self):
        return f"{self.pk}-{self.title}"


class NotificationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    notify_type = models.ForeignKey(NotifyTypeModel, on_delete=models.CASCADE, 
        related_name="notifications_type")
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}-{self.user}-{self.message}"