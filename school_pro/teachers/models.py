from django.db import models
from authentication.models import User


# Create your models here.


class Teacher(models.Model):

    CLASS_OPTIONS = [
        ('CLASS_5', 'CLASS_5'),
        ('CLASS_6', 'CLASS_6'),
        ('CLASS_7', 'CLASS_7'),
        ('CLASS_9', 'CLASS_8'),
        ('CLASS_10', 'CLASS_10')
    ]

    classs = models.CharField(choices=CLASS_OPTIONS, max_length=255)
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField(max_length=255)
    description = models.TextField()
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.owner)+'s income'
