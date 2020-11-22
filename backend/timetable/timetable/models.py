from django.db import models
from django.conf import settings

from .fields import IntegerRangeField


class Teacher(models.Model):
    teacher = models.OneToOneField(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   verbose_name='Логин_преподавателя',
                                   blank=True,
                                   )
    last_name = models.CharField(max_length=50,
                                 verbose_name='Фамилия преподавателя')
    first_name = models.CharField(max_length=50,
                                  verbose_name='Имя преподавателя')
    middle_name = models.CharField(max_length=50,
                                   verbose_name='Отчество преподавателя')
    personal_number = IntegerRangeField(verbose_name='Персональный номер',
                                        primary_key=True,
                                        min_value=100,
                                        max_value=999,
                                        )
    slug = models.SlugField(max_length=250, unique_for_date='last_name')

    class Meta:
        verbose_name_plural = 'Преподаватели'
        verbose_name = 'Преподаватель'
        ordering = ('last_name',)

    def __str__(self):
        return self.last_name
