#!/usr/bin/env python
# coding: utf-8

# ## Testing a shopping cart Using Assert Statements
# 
# The following code shows a shopping cart where items can be added. All items in cart are displayed including their descriptions, quantities and extended price. 
#  
# The goal of this lab is to test the functionality of these classes using assert statements. 
#  
# In the function ```test_cart``` creates an instance of ```Product```, ```LineItem```, and ```Cart```. Once the instance is created use assert statements to verify that the methods work as expected. Refer to “the power of assertions” for details on how to apply asserts in python. 

# In[1]:


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# In[1]:


class LineItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_extended_price(self):
        return self.product.price * self.quantity


# In[2]:


class Cart:
    def __init__(self):
        self.line_items: [LineItem] = []

    def add_product(self, product: Product, quantity: int):
        self.line_items.append(LineItem(product, quantity))

    def get_total(self) -> int:
        total = 0
        for line in self.line_items:
            total += line.product.price * line.quantity

        return total

    def remove(self, line_item_number: int):
        self.line_items.remove(self.line_items[line_item_number - 1])

    def update_quantity(self, line_item_number: int, updated_quantity: int):
        self.line_items[line_item_number - 1].quantity = updated_quantity

    def __str__(self):
        output = []
        for line in self.line_items:
            output.append(f"{line.quantity} {line.product.name} {line.product.price} = {line.get_extended_price()}")
        output.append(f"total: {self.get_total()}")
        return "\n".join(output)


# In[2]:


# test the above classes here using assert methods 

def test_cart():
    """
    Create instances of the above three
    classes, and use assert statements to
    test that they operate as expected.
    """
    pass

