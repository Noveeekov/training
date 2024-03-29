from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest ( TestCase ):
    '''тест домашней страницы'''

    def test_home_page_returns_correct_html ( self ):
        '''тест: домашняя страница возвращает правильный html'''
        response = self.client.get( '/' )
        self.assertTemplateUsed( response, 'home.html' )

