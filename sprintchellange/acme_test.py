#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_number_products(self):
        """Test default product number can be 30"""
        prod1 = generate_products()
        self.assertEqual(len(prod1),30)

    def test_legal_names(self):
        """
        Test all the legal names with nouns & adjectives
        """

        prod1 = generate_products()

        adject = []
        nouns = []

        for i in range(len(prod1)):
            """
            Create a list of all nouns and adjectives 
            """
            nameList = prod1[i].name.split(' ')
            adject.append(nameList[0])
            nouns.append(nameList[1])

        # All product names that have adjectives & nouns
        for i in range(len(adject)):
            self.assertIn(adject[i], ADJECTIVES)

        for i in range(len(nouns)):
            self.assertIn(nouns[i], NOUNS)


if __name__ == '__main__':
    unittest.main()