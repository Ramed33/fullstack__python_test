from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    """Serializa un campo de nombre para nuestra APIView"""
    name = serializers.CharField(max_length=15)