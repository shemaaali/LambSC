# Some import library about the OOP
import random as rm


# Part 1: define a class
class Product:
    """
    Create a class called a Product
    """

    def __init__(self,
                 name,
                 price=10,
                 weight=20,
                 flammability=0.5,
                 identifier=rm.randrange(1000000, 9999999)):
        """
        Define a constructor method to include some fields
        """               

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    # Part 2: define an object
    def stealability(self):
        """
        Define a function is called stealabilit
        To do specific condition and return
        """

        product  = self.price / self.weight

        if product  < 0.5:
            return("Not so stealable...")

        elif (product >= 0.5) & (product < 1.0):
            return("Kinda stealable.")

        else:
            return("Very stealable!")

    def explode(self):
        """
        Define a function is called an explode 

        To calculates the flammability multiple by the weight & return the value for each
        """
        exp = self.weight*self.flammability

        if exp < 10:
            return("...fizzle.")

        elif (exp >= 10) & (exp < 50):
            return("...boom!")

        else:
            return("...BABOOM!!")

# Part 3: define subclass
class BoxingGlove(Product):
    """
    Proper Inheritance subclass from the parent(BoxingGlove)
    """

    def __init__(self,
                 name,
                 price=10,
                 weight=10,
                 flammability=0.5,
                 identifier=rm.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

        super()
    # Override function
    def explode(self):
       
        return("...it's a glove")

    def punch(self):
        """
        Add another subclass called a punch
        which is returned "That tickles."
        """

        if self.weight < 5:
            return('That tickles.')

        elif (self.weight >= 5) & (self.weight < 15):
            return('Hey that hurt!')

        else:
            return('OUCH!')