from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        '''
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        '''
        excepted_html = render_to_string('home.html')
        self.assertEquals(response.content.decode(), excepted_html)