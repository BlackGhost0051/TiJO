import unittest

from Lab2.src.ShoppingCart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.shoppingCart = ShoppingCart()


    def tearDown(self):
        self.shoppingCart = None

    def test_add_product(self):
        product_name = "Apple"
        price = 2
        quantity = 3

        result = self.shoppingCart.add_product(product_name, price, quantity)
        products = self.shoppingCart.get_products()

        self.assertTrue(result)
        self.assertIn("Apple", products)


    def test_remove_product(self):
        product_name = "Banana"
        price = 1
        quantity = 5


        self.shoppingCart.add_product(product_name, price, quantity)

        result = self.shoppingCart.remove_product("Banana")
        products = self.shoppingCart.get_products()

        self.assertTrue(result)
        self.assertNotIn("Banana", products)


    def test_update_quantity(self):
        product_name = "Orange"
        price = 3
        quantity = 2
        new_quantity = 5

        self.shoppingCart.add_product(product_name, price, quantity)


        result = self.shoppingCart.update_quantity(product_name, new_quantity)
        product_quantity = self.shoppingCart.products["Orange"]["quantity"]


        self.assertTrue(result)
        self.assertEqual(product_quantity, 5)


    def test_get_total_price(self):
        product_name = "Grapes"
        price = 4
        quantity = 2

        self.shoppingCart.add_product(product_name, price, quantity)

        prices = self.shoppingCart.get_total_price()

        self.assertEqual(prices, 8)


    def test_apply_discount_code(self):
        product_name = "Mango"
        price = 10
        quantity = 2


        self.shoppingCart.add_product(product_name, price, quantity)
        self.shoppingCart.apply_discount_code("DISCOUNT10")


        prices = self.shoppingCart.get_total_price()


        self.assertEqual(prices, 18)


    def test_checkout(self):
        product_name = "Peach"
        price = 5
        quantity = 1


        self.shoppingCart.add_product(product_name, price, quantity)

        result = self.shoppingCart.checkout()
        products_count = self.shoppingCart.count_products()

        self.assertTrue(result)
        self.assertEqual(products_count, 0)



if __name__ == '__main__':
    unittest.main()