from django.contrib import admin

from .parser import Parser
from .models import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Settings django-admin for new teacher table"""
    list_display = ('__str__', 'user', 'personal_number',)
    search_fields = ('last_name', 'first_name', 'middle_name',)
    ordering = ('first_name', 'last_name', 'middle_name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Settings django-admin for lesson table
    which state page max=30
    """
    list_display = ('date', 'time', 'group', 'subject', 'get_employment', 'get_teacher', 'get_classroom')
    list_filter = ('time', 'group', 'subject', 'teacher', 'classroom')
    ordering = ('date', 'time', 'group')
    date_hierarchy = 'date'
    filter_horizontal = ('teacher', 'classroom', 'employment')
    list_per_page = 30


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Settings django-admin for student group table"""
    list_display = ('number_group', 'type_group',)
    list_filter = ('number_group', 'type_group',)
    search_fields = ('number_group', 'type_group',)
    ordering = ('number_group', 'type_group',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """Settings django-admin for subject table"""
    list_display = ('name_subject',)
    ordering = ('name_subject',)


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    """Settings django-admin for employment table"""
    list_display = ('type_subject', 'number_subject')
    list_filter = ('type_subject', 'number_subject')
    search_fields = ('type_subject', 'number_subject')
    ordering = ('type_subject', 'number_subject')


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    """Settings django-admin for classroom table"""
    list_display = ('number_classroom',)
    ordering = ('number_classroom',)


class ExportCsvMixin:
    """Mixin for created new button in context menu for parsing excel file"""
    def export_in_database(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        for obj in queryset:
            parser = Parser([getattr(obj, field) for field in field_names])
            parser.create_lessons()
    export_in_database.short_description = "Загрузить расписание в базу данных"


@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin, ExportCsvMixin):
    """
    Settings django-admin for excel file table
    which implement new button for parsing
    """
    list_display = ('updated', 'upload')
    actions = ["export_in_database"]
