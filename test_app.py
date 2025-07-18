import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_data(self):
        response = self.app.get('/')
        data = response.get_json()
        self.assertEqual(data['message'], 'Hello from CI/CD Demo App!')
        
    def test_health_endpoint(self):
        response = self.app.get('/health')
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')
        
if __name__ == '__main__':
    unittest.main()
