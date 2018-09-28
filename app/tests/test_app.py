import unittest
import os
import sys 

from app import app




class TestFoodApi(unittest.TestCase):

    def setUp(self):
        self.app = self.test_get
        self.client = self.app.test_client
    
    # GET all orders
    def test_get(self):
        response = self.client().get('/v1/orders')
        self.assertEqual(response.status_code, 200)

    

    def test_post(self):
        pass

    def test_delete(self):
        pass

    def test_put(self):
        pass
        


if __name__ == '__main__':
    unittest.main()
