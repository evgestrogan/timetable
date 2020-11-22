from django.contrib import admin
from .models import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Settings django-admin for new user table"""
    list_display = ('__str__', 'user', 'personal_number',)
    search_fields = ('last_name', 'first_name', 'middle_name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'group', 'subject', 'get_employment', 'get_teacher', 'get_classroom')
    list_filter = ('time', 'group', 'subject', 'teacher', 'classroom')
    ordering = ('date', 'time', 'group')
    date_hierarchy = 'date'
    filter_horizontal = ('teacher', 'classroom', 'employment')
    list_per_page = 100


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('number_group', 'type_group',)
    list_filter = ('number_group', 'type_group',)
    search_fields = ('number_group', 'type_group',)
    ordering = ('number_group', 'type_group',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name_subject',)
    ordering = ('name_subject',)
    # inlines = [Inline]


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('type_subject', 'number_subject')
    list_filter = ('type_subject', 'number_subject')
    search_fields = ('type_subject', 'number_subject')
    ordering = ('type_subject', 'number_subject')


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number_classroom',)
    ordering = ('number_classroom',)
