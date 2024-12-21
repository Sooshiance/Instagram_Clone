from django.db import models

from user.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    caption = models.TextField()
    likes = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    views = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def album(self):
        return Album.objects.filter(post=self)

    def __str__(self):
        return f"{self.user.username} - {self.caption[:15]}"

class Like(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       post = models.ForeignKey(Post, on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)

       class Meta:
           unique_together = ('user', 'post')

class Album(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='album')
    image = models.ImageField(upload_to='album/')

    def __str__(self):
        return f"Album for Post: {self.post.pk}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.body[:15]}"
