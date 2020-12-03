from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LessonList, CourseList, GroupList


app_name = 'api'

urlpatterns = [
    path('lessons/', LessonList.as_view()),
    path('listcourse/', CourseList.as_view()),
    path('listgroups/<str:type_group>', GroupList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)