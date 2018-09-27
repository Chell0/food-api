import unittest
import requests

import responses

class ApiTestCase(unittest.TestCase):
    

    def test_get(self):
        responses.add(**{
            'method' : responses.GET,
            'url' : 'http://127.0.0.1:5000/v1/orders',
            'body' : '{"error": "reason"}',
            'status' : 404,
            'content_type' : 'application/json'
        })

        response = requests.get('http://127.0.0.1:5000/v1/orders')

        self.assertEqual({'error': 'reason'}, response.json())
        self.assertEqual(404, response.status_code)

    

if __name__ == '__main__':
    unittest.main()
