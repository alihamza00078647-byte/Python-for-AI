import numpy as np
""" Manual Way To solve the Problem """

prices = [100, 200, 300, 400] #Product Prices 
discount = 10 # 10% discount
final_Price = []

for price in prices:
    newPrice = price - ((price * discount) /100)
    final_Price.append(newPrice)
print(final_Price)

""" Broadcasting way to solve the problem with Loops ( that makes programs slow) """
""" **__Different shapes ke arrays ko automatically stretch karke operate karo__** """

prices = np.array([100, 200, 300, 400])
discount = 10
finalPrices = prices - (prices * discount / 100)
print(finalPrices)



