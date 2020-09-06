#!/usr/bin/python
import math

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.collection = collection
    self.items_per_page = items_per_page
  
## returns the number of items within the entire collection
  def item_count(self):
    return len(self.collection)

## returns the number of pages
  def page_count(self):
    return int(math.ceil(self.item_count() / int(self.items_per_page)))

## returns the number of items on the current page. page_index is zero based
## this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    if int(page_index) == self.page_count() - 1:
      return self.item_count() % self.items_per_page
    if page_index not in range(0,self.page_count()):
      return int(-1)
    else:
      return int(self.items_per_page)

## determines what page an item is on. Zero based indexes.
## this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    if int(item_index) not in range(0, self.item_count()):
      return int(-1)
    else:
      return int(int(item_index + 1) / int(self.items_per_page))

p1 = PaginationHelper([1,2,3,4,5], 2)
print(f"""
      My input array is {p1.collection} with {p1.items_per_page} items per page.
      There are {p1.item_count()} items in the array on {p1.page_count()} pages.
      On page 3 there are {p1.page_item_count(2)} item(s).
      The 3rd value is on page {p1.page_index(2) + 1} and the 5th value is on page {p1.page_index(4) + 1}.
      """)