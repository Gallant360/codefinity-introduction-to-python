grocery_items = "milk cheese bread apples oranges chicken"
dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[11:17]
grocery = dairy1 + " " +dairy2
aisle = dairy1
item = dairy2
bakery = bakery1
answer = (f"we have dairy and bakery items: {aisle}, {item}, and {bakery} in aisle 5")
print(answer)