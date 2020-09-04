from acme import Product
import random as rm


# Part 4 - Class Report
def generate_products(x=30):
    """
    Generate number of products represents as x 
    Randomly return the number of products into list.
    """
    adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    name = [rm.choice(adjectives) + " " + rm.choice(nouns) for i in range(x)]
    price = [rm.choice([i for i in range(5, 100)]) for i in range(x)]
    weight = [rm.choice([i for i in range(5, 100)]) for i in range(x)]
    flammability = [round(rm.uniform(0.0, 2.5)) for i in range(x)]
    products = [[name[i], price[i], weight[i],
                 flammability[i]] for i in range(x)]
    return products


def inventory_report(products):
    """
    Report and calculate Number of unique product names into  the product list
    Average(mean)price, weight, and flammability as a list for products
    """
    nunique = len(set(i[0] for i in products))
    avgprice = sum(i[1] for i in products) / len(products)
    avgweight = sum(i[2] for i in products) / len(products)
    avgflammability = sum(i[3] for i in products) / len(products)
    
    print("Acme Corporation Official Inventory Report:")
    print("Unique Product Names:", nunique)
    print("Average Or Mean Price:", avgprice)
    print("Average Or Mean Weight:", avgweight)
    print("Average Or Mean Flammability", avgflammability)


if __name__ == '__main__':
    inventory_report(generate_products())