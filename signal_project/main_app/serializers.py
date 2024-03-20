from rest_framework import serializers
from main_app.models import post, Category, Tag
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author_details = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = post
        fields = ['id', 'title', 'body', 'author', 'categories', 'tags', 'author_details']

    def get_author_details(self, obj):
        return {
            'username': obj.author.username,
            'email': obj.author.email,
        }

