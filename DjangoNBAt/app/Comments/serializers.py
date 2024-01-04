from rest_framework import serializers
from .models import Comment
from matches.serializers import MatchesSerializer

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'match',
            'content',
            'created_at')