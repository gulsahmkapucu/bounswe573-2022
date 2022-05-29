from ast import arg
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from learnwithus.views import *

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url=reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_list_page_url_resolves(self):
        url=reverse('courses')
        self.assertEquals(resolve(url).func, list_page)

    def test_register_url_resolves(self):
        url=reverse('accounts/register')
        self.assertEquals(resolve(url).func.view_class, RegisterPage)    
    
    def test_profile_url_resolves(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func.view_class, ProfileView)

    def test_search_url_resolves(self):
        url=reverse('searchbar')
        self.assertEquals(resolve(url).func.view_class, SearchView)

    def test_course_detail_resolves(self):
        url=reverse('coursedetail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, CourseDetail)
    
    def test_login_resolves(self):
        url=reverse('accounts/login')
        self.assertEquals(resolve(url).func.view_class, LoginView)