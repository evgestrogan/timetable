from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LessonList


app_name = 'api'

urlpatterns = [
    path('lessons/', LessonList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)