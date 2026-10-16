import numpy as np

"""
Random Walk aik aisi mathematical simulation hai jahan har agla qadam (step) bilkul random hota hai—yaani agla qadam kahan hoga, iska pichle qadamon se koi lena dena nahi hota.
"""

# how many times generate numbers 
steps = 10

# generate random choice from -1 to n
random = np.random.choice([-1, 6], size=steps)

# track and remember the random steps 
track_randomness = np.cumsum(random)

print(random)
print(track_randomness)
