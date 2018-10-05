import unittest

class TestApp(unittest.TestCase):
    """The parent class"""

    def setUp(self):
        """SetUp"""
        # self.app = app.OrderList()
        # self.app = app.Order()
        pass

    def tearDown(self):
        """Teardown"""
        pass

    def test_get(self):
        """Test the GET all request"""
        # response = self.app.get('/v1/orders')
        # print(response.data)
        pass

    def test_get_one(self):
        """Test to retrieve a single order"""
        # response = requests.get('/v1/orders/<int:id>')
        # assert response.text == "Your order was found"
        pass

    def test_create_order(self):
        """Test the creation of orders"""
        # response = self.app.post('/v1/orders')
        # print(response.data)
        pass

    def test_update_order(self):
        """Test updating the order status"""
        # response = self.app.update('/v1/orders/<int:id>')
        # print(response.data)
        pass

    def test_delete_order(self):
        """Test delete an order by id"""
        # response = self.app.delete('/v1/orders/<int:id>')
        # assert isinstance(response.data, object)
        # print(response.data)
        pass
