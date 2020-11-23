from rest_framework import serializers


class EmploymentSerializer(serializers.Serializer):
    number_subject = serializers.CharField()
    type_subject = serializers.CharField()