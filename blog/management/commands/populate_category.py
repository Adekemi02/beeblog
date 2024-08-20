from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    help = 'Populate the Category model with initial data'

    def handle(self, *args, **kwargs):
        categories = [
            {'name': 'Technology', 'description': 'Posts related to technology.'},
            {'name': 'Health', 'description': 'Posts related to health and wellness.'},
            {'name': 'Lifestyle', 'description': 'Posts about lifestyle and personal experiences.'},
        ]
        
        for cat in categories:
            Category.objects.get_or_create(name=cat['name'], description=cat['description'])
        self.stdout.write(self.style.SUCCESS('Successfully populated categories'))