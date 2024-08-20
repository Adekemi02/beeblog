from django.contrib import admin
from .models import BlogPost, Comment, Category


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')

    
admin.site.register(BlogPost, BlogModelAdmin)
admin.site.register(Category)
admin.site.register(Comment)
