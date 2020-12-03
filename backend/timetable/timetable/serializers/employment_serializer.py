from rest_framework import serializers


class EmploymentSerializer(serializers.Serializer):
    """Serializer for lesson serializer"""
    number_subject = serializers.CharField()
    type_subject = serializers.CharField()
