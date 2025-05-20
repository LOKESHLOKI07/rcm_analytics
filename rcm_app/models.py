from django.db import models


from django.contrib.auth.models import User  # Add this import

class ExcelUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # NEW
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255)
    row_count = models.PositiveIntegerField()
    columns = models.JSONField()

    def __str__(self):
        return f"{self.file_name} ({self.row_count} rows)"


class ExcelData(models.Model):
    upload = models.ForeignKey(ExcelUpload, on_delete=models.CASCADE, related_name='rows')
    data = models.JSONField()  # Stores all row data

    def __str__(self):
        return f"Row from {self.upload.file_name}"

    def get_field(self, field_name):
        return self.data.get(field_name)

from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room for: {', '.join([user.username for user in self.users.all()])}"

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} at {self.timestamp}"
