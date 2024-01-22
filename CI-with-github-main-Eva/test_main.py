import unittest
from app import app



class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello(self):
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'hello': 'world'})

    def test_hello_name(self):
        response = self.app.get('/api/hello/ben')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'hello': 'ben'})

    def test_whoami(self):
        response = self.app.get('/api/whoami')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['ip'])

    def test_whoami_name(self):
        response = self.app.get('/api/whoami/ben')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'ben')

if __name__ == '__main__':
    unittest.main()
