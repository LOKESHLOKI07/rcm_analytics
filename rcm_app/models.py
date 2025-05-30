from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    phone = models.CharField(max_length=15)
    avg_claim_rate_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    heard_about_us = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username




class ExcelUpload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255)
    row_count = models.PositiveIntegerField()
    columns = models.JSONField()

    def __str__(self):
        return f"{self.file_name} ({self.row_count} rows)"


class ExcelData(models.Model):
    upload = models.ForeignKey(ExcelUpload, on_delete=models.CASCADE, related_name='rows')
    data = models.JSONField()

    def __str__(self):
        return f"Row from {self.upload.file_name}"


class ChatRoom(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room for: {', '.join(user.username for user in self.users.all())}"


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} at {self.timestamp}"
