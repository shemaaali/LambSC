import unittest
from acme import Product
from acme_report import generate_products
import random as rm


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight can be 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default flammability being 0.5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability_and_expode(self):
        """Test functionality of stealability and explode methods"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...boom!')

    def test_identifier_functionality(self):
        """Test identifier function properly"""
        prod = Product('Test Product')
        self.assertTrue(1000000 <= prod.identifier <= 10000000)


class AcmeReportTests(unittest.TestCase):
    """Test Acme Report Properly"""
    def test_default_num_products(self):
        """Test default number of products"""
        generated_products = generate_products()
        self.assertEqual(len(generated_products), 30)

    def test_legal_names(self):
        """
        Test all the legal names with nouns & adjectives
        """
        adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        adjn = adjectives + nouns
        product_names = [i[0] for i in generate_products()]
        
        # All product names that have adjectives & nouns
        for x in product_names:
            na = x.split()
            for i in na:
                self.assertIn(i, adjn)


if __name__ == '__main__':
    unittest.main()