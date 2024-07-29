from rest_framework import serializers
from rest_framework.permissions import AllowAny


class GetInfo(serializers.Serializer):
    name = serializers.CharField()
