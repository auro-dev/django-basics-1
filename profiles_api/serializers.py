from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name filed """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

class UserPostsSerializer(serializers.ModelSerializer):
    """Serializes a user posts object"""


class FollowSerializer(serializers.ModelSerializer):
    """Serializes a follow object"""

class SaveSerializer(serializers.ModelSerializer):
    """Serializes a save object"""
    