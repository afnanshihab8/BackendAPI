from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Show user details in response

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'product']

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Include comments

    class Meta:
        model = Product
        fields = '__all__'
