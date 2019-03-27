from django.test import TestCase, RequestFactory
from .models import Book


class TestBookaModels(TestCase):
    def setUp(self):
        Book.objects.create(title='title one', author='author one', year=1901)
        Book.objects.create(title='title two', author='author two', year=1902)
        Book.objects.create(title='title three', author='author three', year=1903)

    def test_book_titles(self):
        one = Book.objects.get(title='title one')
        two = Book.objects.get(title='title two')
        self.assertEqual(one.title, 'title one')
        self.assertEqual(two.title, 'title two')

    def test_book_author(self):
        one = Book.objects.get(title='title one')
        two = Book.objects.get(title='title two')
        self.assertEqual(one.author, 'author one')
        self.assertEqual(two.author, 'author two')

    def test_book_year(self):
        one = Book.objects.get(title='title one')
        two = Book.objects.get(title='title two')
        self.assertEqual(one.year, 1901)
        self.assertEqual(two.year, 1902)
        


class TestNotesViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        Book.objects.create(title='title one', author='author one', year='1901')
        Book.objects.create(title='title two', author='author two', year='1902')
        Book.objects.create(title='title three', author='author three', year='1903')



    def test_book_detail_view_context(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{Book.objects.get(title="title one").id }')
        self.assertIn(b'author one', response.content)

    def test_book_list_view_context(self):
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(b'title two', response.content)

    def test_book_detail_view_status_code_success(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{ Book.objects.get(title="title one").id }')
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_status_code_success(self):
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view_status_code_failure(self):
        from .views import book_detail_view
        from django.http import Http404
        request = self.request.get('')
        with self.assertRaises(Http404):
            book_detail_view(request, '0')
