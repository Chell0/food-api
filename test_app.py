import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def setUp(self, Flask=None):
        self.app = Flask(__name__)
        self.client = self.app.test_client
        self.order = {'title': 'Chicken Burger'}

    def test_order_creation(self):
        create = self.client.post('/orders/', data=self.order)
        self.assertEqual(request.status_code, 201)
        self.assertIn('Chicken Burger', str(request.data))

    def test_the_get_all_orders_request(self):
        request = self.client.get('/orders/')
        self.assertEqual(request.status_code, 200)
        self.assertIn('Chicken Burger', str(request.data))

    def test_api_to_get_an_order_by_id(self):
        id = self.client.get('/orders/', data=order_id)
        self.assertEqual(request.status_code, 200)
        self.assertIn('Chicken Burger', str(request.data))

    def test_if_order_can_be_updated(self):
        update = self.client.update('/orders/', data=order_id.replace(""),
                                    result=self.client.get('/orders/{}'.format(result_in_json['id'])))
        self.assertEqual(request.status_code, 200)
        self.assertIn('Chicken Burger', str(request.data))


if __name__ == '__main__':
    unittest.main()
