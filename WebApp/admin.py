from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'marks', 'created_at']
    list_filter = ['subject', 'marks', 'created_at']
    search_fields = ['name', 'subject']
    ordering = ['-created_at']
    list_per_page = 20