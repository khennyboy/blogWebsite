from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(default='')
    image = models.TextField(default='', blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        # Get all comments related to this post, including replies
        return Comment.objects.filter(post=self).count()
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user} -- {self.content}"
    
class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eachLikes')
    eachpost = models.ForeignKey(Post, related_name='userslikes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'eachpost')  

    def __str__(self):
        return f"{self.user.username} likes {self.eachpost.title}"
    
