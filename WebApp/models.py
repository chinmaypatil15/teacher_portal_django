from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.marks})"
    
    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'subject'],
                name='unique_student_subject',
                violation_error_message='Student already exists for this subject'
            )
        ]
