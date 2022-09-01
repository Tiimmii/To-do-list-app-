from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Task(models.Model):
    TASK_CHOICES=(
        ('complete', 'Complete'),
        ('incomplete','Incomplete'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=TASK_CHOICES, max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


