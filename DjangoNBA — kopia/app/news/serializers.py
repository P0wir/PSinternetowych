from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.ModelSerializer):
    publication_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = News
        fields = (
            'title',
            'content',
            'author',
            'publication_date'
        )