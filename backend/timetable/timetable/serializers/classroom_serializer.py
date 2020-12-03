from rest_framework import serializers


class ClassroomSerializer(serializers.Serializer):
    """Serializer for lesson serializer"""
    number_classroom = serializers.CharField()
