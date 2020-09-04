#!/usr/bin/env python
import random as rm
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    Generate number of products represents as x 
    Randomly return the number of products into list.
    """

    products = []

    for prod in range(num_products):

        adj = rm.sample(ADJECTIVES, k=1)[0]
        noun = rm.sample(NOUNS, k=1)[0]
        name = f'{adj} {noun}'
        price = rm.randint(5, 100)
        weight = rm.randint(5, 100)
        flammability = rm.uniform(0.0, 2.5)

        prod = Product(name,
                       price=price,
                       weight=weight,
                       flammability=flammability
                       )

        products.append(prod)

    return(products)


def inventory_report(products):
    """
    Report and calculate Number of unique product names into  the product list
    Average(mean)price, weight, and flammability as a list for products
    """

    names = []
    weights = []
    prices = []
    flams = []

    for i in range(len(products)):
        names.append(products[i].name)
        weights.append(products[i].weight)
        prices.append(products[i].price)
        flams.append(products[i].flammability)

    nunique= len(set(names))
    avgprice = sum(prices)/len(prices)
    avgweight = sum(weights)/len(weights)
    avgflammability = sum(flams)/len(prices)

     
    print("Acme Corporation Official Inventory Report:")
    print("Unique Product Names:", nunique)
    print("Average Or Mean Price:", avgprice)
    print("Average Or Mean Weight:", avgweight)
    print("Average Or Mean Flammability", avgflammability)


if __name__ == '__main__':
    inventory_report(generate_products())