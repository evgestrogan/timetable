from rest_framework import serializers


class TeacherSerializer(serializers.Serializer):
    """Serializer for lesson serializer"""
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
