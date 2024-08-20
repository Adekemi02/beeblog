from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name




class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created_at',)

    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    name = models.CharField(max_length=100, blank=True, null=True)  # For unregistered users
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.content