from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import BlogPost

# Create your tests here.
class BlogTests(TestCase):
    
   def setUp(self):
      self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
      self.post = BlogPost.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )
   def test_string_representation(self):
      post = BlogPost(title = "A sample title")
      self.assertEqual(str(post), post.title)
   
   def test_post_content(self):
      self.assertEqual(f'{self.post.title}', 'A good title')
      self.assertEqual(f'{self.post.body}', 'Nice body content')
      self.assertEqual(f'{self.post.author}', 'testuser')
   
   def test_post_list_view(self):
      response = self.client.get(reverse('blog'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'Nice body content')
      self.assertTemplateUsed(response, 'blog.html')

   def test_post_detail_view(self):
      response = self.client.get('/blog/1/')
      no_response = self.client.get('/blog/1000/')
      self.assertEqual(response.status_code, 200)
      self.assertEqual(no_response.status_code, 404)
      self.assertContains(response, 'A good title')
      self.assertTemplateUsed(response, 'post_detail.html')
   