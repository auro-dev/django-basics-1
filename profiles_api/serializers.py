from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name filed """
    name = serializers.CharField(max_length=10)




class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    