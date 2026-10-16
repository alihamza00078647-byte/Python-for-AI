import numpy as np


# aik random array generate kiya hai.
y = np.random.randint(1, 7, size=10)

# aik random array generate kar ke pass kiya hai.
x = np.array(y)

# count karta hai ke integer kitni baar aya hai array mein 
counts = np.bincount(x)

# check kary ga kon sa number zyada baar aya hai
max_arg = np.argmax(counts)


print(max_arg)



