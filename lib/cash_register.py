#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []


  def add_item(self,title,price,quantity = 1):
    self.transactions.append(dict(title = price * quantity))
    self.total += price * quantity
    if quantity == 1:
      self.items.append(title)
    else:
      new_item = list()
      new_item.append(title)
      multiples = new_item * quantity
      for item in multiples:
        self.items.append(item)

    return self.items

  def apply_discount(self):
    if self.discount > 0:
      discount = self.total * (self.discount/100)
      self.total = int(self.total - discount)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    last_transaction = self.transactions[-1]['title']
    self.total = self.total - last_transaction