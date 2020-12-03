from datetime import datetime, timedelta

from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from .serializers.lesson_serializer import LessonSerializer
from .serializers.group_serializer import NumberGroupSerializer
from rest_framework.response import Response
from .models import Lesson, Group

def create_week(date):
    year, month, day = date.split('-')
    today = datetime(day=int(day), month=int(month), year=int(year))
    week_number = today.date().weekday()
    date_start = today - timedelta(days=week_number)
    date_end = today + timedelta(days=6 - week_number)
    return str(date_start.date()), str(date_end.date())


class LessonList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        date = request.query_params['date']
        try:
            number_group = request.query_params['number_group']
            lessons = Lesson.objects.filter(group=number_group, date__range=(create_week(date)))
        except:
            personal_number = request.query_params['personal_number']
            lessons = Lesson.objects.filter(teacher__personal_number=personal_number, date__range=(create_week(date)))
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class CourseList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        courses = {}
        groups = Group.objects.all().filter(type_group__endswith='Курс')
        for group in groups:
            type = group.type_group
            if type not in courses.values():
                courses[len(courses) + 1] = type
        return JsonResponse(courses)


class GroupList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get_object(self, type_group):
        try:
            return Group.objects.filter(type_group=type_group)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, type_group, format=None):
        if type_group == 'Listener':
            groups = self.get_object('Слушатели')
        elif type_group == 'Course':
            groups = self.get_object('Группа ПК')
        elif type_group.isnumeric():
            groups = self.get_object(str(type_group) + ' Курс')
        else:
            raise Http404
        serializer = NumberGroupSerializer(groups, many=True)
        return Response(serializer.data)


