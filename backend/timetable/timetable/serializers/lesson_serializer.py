from rest_framework import serializers
from .employment_serializer import EmploymentSerializer
from .classroom_serializer import ClassroomSerializer
from .teacher_serializer import TeacherSerializer


class LessonSerializer(serializers.Serializer):
    group = serializers.CharField()
    subject = serializers.CharField()
    employment = EmploymentSerializer(many=True, read_only=True)
    classroom = ClassroomSerializer(many=True, read_only=True)
    teacher = TeacherSerializer(many=True, read_only=True)
    time = serializers.CharField()
    date = serializers.DateField()