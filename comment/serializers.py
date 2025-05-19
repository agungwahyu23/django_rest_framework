from rest_framework import serializers
from .models import Post
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = '__all__'