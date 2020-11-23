from rest_framework import serializers


class ClassroomSerializer(serializers.Serializer):
    number_classroom = serializers.CharField()