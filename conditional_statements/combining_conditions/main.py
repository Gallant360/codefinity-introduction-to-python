# The item's discount and stock status have been defined
discounted = False
lowStock = True
low_stock = discounted or lowStock
discounted_stock = not lowStock 
movingProduct = True 
promotion = False  
print("is the item eligible for promotion?", promotion)