from ..v1.app import app
import unittest



class TestFoodApi(unittest.TestCase):
    
    # GET all orders
    def test_get(self):
        tester = app.test_client(self)
        reponse = tester.get('/v1/orders', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    

    # def test_post(self):

    # def test_delete(self):

    # def test_put(self):
        



if __name__ == '__main__':
    unittest.main()