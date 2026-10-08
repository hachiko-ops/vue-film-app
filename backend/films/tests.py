from django.test import TestCase

# Create your tests here.

class SearchViewTests(TestCase):
    def test_search_view_no_param(self):
        response = self.client.get('/api/films/search')
        print(response.content)  # Print the response content for debugging
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Search parameter is required')

    def test_search_view_short_param(self):
        response = self.client.get('/api/films/search?s=ab')
        print(response.content)  # Print the response content for debugging
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Search parameter must be at least 3 characters long')

    def test_search_view(self):
        response = self.client.get('/api/films/search?s=Vorrei vedere un film commedia degli anni 80')
        print(response.content)  # Print the response content for debugging
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'Inception')

