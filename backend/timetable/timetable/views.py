from rest_framework.views import APIView
from .serializers.lesson_serializer import LessonSerializer
from rest_framework.response import Response
from .models import Lesson


class LessonList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        number_group = request.data['number_group']
        date_start = request.data['date_start']
        date_end = request.data['date_end']
        lessons = Lesson.objects.filter(group=number_group, date__range=(date_start, date_end))
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

