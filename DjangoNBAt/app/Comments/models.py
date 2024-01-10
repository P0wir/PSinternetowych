from django.db import models
from matches.models import Matches
from django.contrib.auth.models import User

class Comment(models.Model):
    match = models.ForeignKey('matches.Matches', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username}'s comment on {self.match} at {self.created_at}"
        else:
            return f"Anonymous comment on {self.match} at {self.created_at}"

class Meta:
    verbose_name = "Comment"
    verbose_name_plural = "Comments"