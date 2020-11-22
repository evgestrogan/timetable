from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Settings django-admin for new user table"""
    list_display = ('personal_number', 'teacher', 'last_name', 'first_name', 'middle_name')
    search_fields = ('username',)
