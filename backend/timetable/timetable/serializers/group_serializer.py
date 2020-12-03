from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    """Serializer for group serializer"""
    type_group = serializers.CharField()


class NumberGroupSerializer(serializers.Serializer):
    """Serializer for number group serializer"""
    number_group = serializers.CharField()
