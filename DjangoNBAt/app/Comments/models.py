from django.db import models
from matches.models import Matches

class Comment(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.match} at {self.created_at}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
