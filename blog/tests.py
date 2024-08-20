from django.test import TestCase, Client
from django.urls import reverse
from .models import BlogPost, Category, Comment
from django.contrib.auth.models import User



class CategoryModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Tech', description='Tech-related posts.')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Tech')

    def test_category_fields(self):
        self.assertEqual(self.category.name, 'Tech')
        self.assertEqual(self.category.description, 'Tech-related posts.')


class BlogPostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Tech', description='Tech-related posts.')
        self.post = BlogPost.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            slug='test-post',
            category=self.category
        )

    def test_blogpost_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_comment_count(self):
        self.assertEqual(self.post.comment_count(), 0)
        Comment.objects.create(user=self.user, post=self.post, content='Test comment')
        self.assertEqual(self.post.comment_count(), 1)

    def test_blogpost_comments(self):
        comment = Comment.objects.create(user=self.user, post=self.post, content='Test comment')
        self.assertIn(comment, self.post.comments())

class CommentModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Tech', description='Tech-related posts.')
        self.post = BlogPost.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            slug='test-post',
            category=self.category
        )
        self.comment = Comment.objects.create(user=self.user, post=self.post, content='Test comment')

    def test_comment_str(self):
        self.assertEqual(str(self.comment), 'Test comment')

    def test_comment_fields(self):
        self.assertEqual(self.comment.content, 'Test comment')
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.post, self.post)