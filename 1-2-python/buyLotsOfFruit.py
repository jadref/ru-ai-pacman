import sys
import re

fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples
            
    Returns cost of order
    """ 
    totalCost = 0.0             
    "*** YOUR CODE HERE ***"
    return totalCost

orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))