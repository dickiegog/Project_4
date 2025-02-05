from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, About, CollaborateRequest, Category
from .forms import CommentForm, CollaborateForm

class ModelTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        # Create a category
        self.category = Category.objects.create(name='Tech')
        # Create a post
        self.post = Post.objects.create(
            title='Test Post',
            body='This is a test post.',
            author=self.user,
            category='Tech',
            status='Published'
        )
        # Create a comment
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a test comment.'
        )
        # Create an About entry
        self.about = About.objects.create(
            title='About Me',
            content='This is a test about section.'
        )
        # Create a collaboration request
        self.collab_request = CollaborateRequest.objects.create(
            name='Test User',
            email='test@example.com',
            message='This is a test collaboration request.'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.status, 'Published')
        self.assertEqual(self.post.category, 'Tech')

    def test_comment_creation(self):
        self.assertEqual(self.comment.body, 'This is a test comment.')
        self.assertEqual(self.comment.post.title, 'Test Post')
        self.assertEqual(self.comment.author.username, 'testuser')

    def test_about_creation(self):
        self.assertEqual(self.about.title, 'About Me')
        self.assertEqual(self.about.content, 'This is a test about section.')

    def test_collaborate_request_creation(self):
        self.assertEqual(self.collab_request.name, 'Test User')
        self.assertEqual(self.collab_request.email, 'test@example.com')
        self.assertEqual(self.collab_request.message, 'This is a test collaboration request.')

    def test_post_str_method(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_comment_str_method(self):
        self.assertEqual(str(self.comment), f"Comment {self.post} by {self.user}")

    def test_about_str_method(self):
        self.assertEqual(str(self.about), 'About Me')

    def test_collaborate_request_str_method(self):
        self.assertEqual(str(self.collab_request), 'Test User - test@example.com')


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            body='This is a test post.',
            author=self.user,
            category='Tech',
            status='Published'
        )
        self.about = About.objects.create(
            title='About Me',
            content='This is a test about section.'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Me')

    def test_comment_form_submission(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('post_detail', args=[self.post.slug]), {
            'body': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(body='This is a test comment.').exists())

    def test_collaborate_form_submission(self):
        response = self.client.post(reverse('about'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test collaboration request.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(CollaborateRequest.objects.filter(message='This is a test collaboration request.').exists())


class FormTests(TestCase):
    def test_comment_form_valid(self):
        form_data = {'body': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_collaborate_form_valid(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test collaboration request.'
        }
        form = CollaborateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {'body': ''}  # Empty body
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_collaborate_form_invalid(self):
        form_data = {
            'name': '',  # Empty name
            'email': 'test@example.com',
            'message': 'This is a test collaboration request.'
        }
        form = CollaborateForm(data=form_data)
        self.assertFalse(form.is_valid())