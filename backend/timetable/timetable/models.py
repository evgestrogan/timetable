from django.db import models
from django.conf import settings

from .fields import IntegerRangeField


class Teacher(models.Model):
    """Table information about teacher."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='Логин преподавателя',
                                blank=True,
                                null=True,
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

    class Meta:
        verbose_name_plural = 'Преподаватели'
        verbose_name = 'Преподаватель'
        ordering = ('last_name', 'first_name')

    def __str__(self):
        """
        Returns the first_name plus the last_name and middle_name.
        """
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)


class Subject(models.Model):
    """Table with subject name."""
    name_subject = models.CharField(max_length=50,
                                    verbose_name='Название предмета',
                                    )

    class Meta:
        verbose_name_plural = 'Предметы'
        verbose_name = 'Предмет'
        ordering = ('name_subject',)

    def __str__(self):
        return self.name_subject

    def __repr__(self):
        return self.name_subject


class Employment(models.Model):
    """Table with type and number subject"""
    EMPLOYMENT_CHOICES = (
        ('Л', 'Лекция'),
        ('ПЗ', 'Практическое занятие'),
        ('С', 'Семинар'),
        ('Зачет', 'Зачет'),
        ('Диф.Зачет', 'Дифференцированный зачет'),
    )
    number_subject = models.CharField(max_length=6,
                                      verbose_name='Номер занятия',
                                      blank=True,
                                      )
    type_subject = models.CharField(max_length=25,
                                    choices=EMPLOYMENT_CHOICES,
                                    verbose_name='Тип занятия',
                                    )

    class Meta:
        ordering = ('type_subject', 'number_subject')
        verbose_name_plural = 'Занятия'
        verbose_name = 'Занятие'

    def __str__(self):
        return '{} {}'.format(self.type_subject, self.number_subject)


class Classroom(models.Model):
    """Table with number classroom"""
    number_classroom = models.CharField(max_length=20,
                                        verbose_name='Номер аудитории',
                                        primary_key=True,
                                        )

    class Meta:
        verbose_name_plural = 'Аудитории'
        verbose_name = 'Аудитория'
        ordering = ('number_classroom', )

    def __str__(self):
        return self.number_classroom


class Group(models.Model):
    """Table student group with number and type group"""
    number_group = models.CharField(max_length=5,
                                    verbose_name='Номер группы',
                                    primary_key=True,
                                    )
    type_group = models.CharField(max_length=20,
                                  verbose_name='Тип группы',
                                  help_text='Например: "Группа ПК", "Слушатели" или "1 Курс"',
                                  )

    class Meta:
        ordering = ('number_group',)
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'

    def __str__(self):
        return self.number_group


class Lesson(models.Model):
    """Main table which include all information about lesson"""
    TIME_LESSON_CHOICES = (
        ('1-2', '1-2 час'),
        ('3-4', '3-4 час'),
        ('5-6', '5-6 час'),
        ('7-8', '7-8 час')
    )
    group = models.ForeignKey(Group,
                              on_delete=models.CASCADE,
                              verbose_name='Группа',
                              )
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                verbose_name='Название предмета',
                                )
    employment = models.ManyToManyField(Employment,
                                        verbose_name='Занятие',
                                        blank=True,
                                        )
    classroom = models.ManyToManyField(Classroom,
                                       verbose_name='Номер аудитории',
                                       )
    teacher = models.ManyToManyField(Teacher,
                                     verbose_name='Преподаватель',
                                     blank=True,
                                     )
    time = models.CharField(max_length=10,
                            choices=TIME_LESSON_CHOICES,
                            )
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'
        ordering = ('date', 'time')
        unique_together = (('date', 'time', 'group'),)

    def get_teacher(self):
        """Return list teachers for m2m relation"""
        return ", ".join([str(p) for p in self.teacher.all()])

    def get_classroom(self):
        """Return list classrooms for m2m relation"""
        return ", ".join([str(p) for p in self.classroom.all()])

    def get_employment(self):
        """Return list employments for m2m relation"""
        return ", ".join([str(p) for p in self.employment.all()])

    def __str__(self):
        return '{} {} - {} - {}'.format(self.date, self.time, self.subject, self.group)
