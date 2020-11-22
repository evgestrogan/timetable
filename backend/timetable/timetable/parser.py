import re
import xlrd as xlrd

from .models import *


class TimeTableParser():
    def __init__(self, path):
        wb = xlrd.open_workbook(str(path))
        self.sheet = wb.sheet_by_index(len(wb.sheet_names()) - 1)

    def is_digit(self, string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False

    def list_date(self, start_row, column):
        for row in range(start_row, self.sheet.nrows):
            value = str(self.sheet.cell_value(row, column))
            if re.search(r'(\d{2}.\d{2}.\d{4})', value):
                yield value, row, column

    def list_groups(self, row, start_column):
        for column in range(start_column, self.sheet.ncols):
            value = str(self.sheet.cell_value(row, column))
            if self.is_digit(value):
                yield value, row, column
            else:
                break

    def list_time(self, start_row, column):
        times = []
        for row in range(start_row, self.sheet.nrows):
            value = str(self.sheet.cell_value(row, column))
            if re.search(r'(\d{1}-\d{1})', value) and value not in times:
                times.append(value)
                yield value, row, column

    def list_lesson(self, start_row, column):
        for row in range(start_row, start_row + 4):
            yield str(self.sheet.cell_value(row, column))

    def timetable(self):
        for row in range(self.sheet.nrows):
            for column in range(self.sheet.ncols):
                value = str(self.sheet.cell_value(row, column))
                if value == 'Дата':
                    for date in self.list_date(row, column):
                        for time in self.list_time(date[1], date[2] + 1):
                            for group in self.list_groups(row, column + 2):
                                timetable = [date[0], time[0], group[0]]
                                for lesson in self.list_lesson(time[1], group[2]):
                                    timetable.append(lesson)
                                yield timetable


class Parser():
    def __init__(self, path):
        self.path = path
        self.timetable = TimeTableParser(self.path[1])

    def get_type_froup(self, group):
        if group.startswith('1') and group.isnumeric():
            return group[1] + ' Курс'
        elif not group.isnumeric():
            return 'Группа ПК'
        elif group.startswith('2') and group.isnumeric():
            return 'Слушатели'

    def get_employment_list(self, employments):
        for employment in employments.split(';'):
            if employment != '':
                try:
                    type_subject, number_subject = employment.split(' ')
                except ValueError:
                    type_subject = employment
                    number_subject = ''
                yield Employment.objects.get_or_create(type_subject=type_subject, number_subject=number_subject)[0]

    def get_teacher_list(self, teachers):
        for teacher in teachers.split(' '):
            if teacher != '':
                yield Teacher.objects.get_or_create(last_name=teacher)[0]

    def get_classroom_list(self, classrooms):
        for classroom in classrooms.split(' '):
            if classroom != '':
                yield Classroom.objects.get_or_create(number_classroom=classroom)[0]

    def create_lessons(self):
        for date, time, group, subject, employments, teachers, classrooms  in self.timetable.timetable():
            type_group = self.get_type_froup(group)
            obj_employments = self.get_employment_list(employments)
            obj_teachers = self.get_teacher_list(teachers)
            obj_classrooms = self.get_classroom_list(classrooms)

            lesson = Lesson.objects.get_or_create(date='-'.join(reversed(date.split('.'))),
                                                  time=time,
                                                  subject=Subject.objects.get_or_create(name_subject=subject)[0],
                                                  group=Group.objects.get_or_create(number_group=group, type_group=type_group)[0],
                                                  )[0]
            for teacher in obj_teachers:
                lesson.teacher.add(teacher)
            for classroom in obj_classrooms:
                lesson.classroom.add(classroom)
            for employment in obj_employments:
                lesson.employment.add(employment)
