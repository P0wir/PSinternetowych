from rest_framework import serializers
from .models import Comment
from matches.serializers import MatchesSerializer

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'match',
            'content',
            'created_at')

    def get_user(self):
        if self.context['request'].user.is_authenticated:
            return self.context['request'].user.username
        else:
            return "anonymous"
