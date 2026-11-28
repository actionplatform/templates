"""The contract of every request and response."""

from rest_framework import serializers


class ItemCreateSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=True, trim_whitespace=False)


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
