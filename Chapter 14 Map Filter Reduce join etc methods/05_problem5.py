from functools import reduce
tup = (132, 34,455, 6,7,8, 3)

def maximum(x, y):
    if x> y:
        return x
    return y


num = reduce(maximum, tup)
print(num)