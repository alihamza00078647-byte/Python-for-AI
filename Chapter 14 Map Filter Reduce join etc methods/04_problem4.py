l = [3, 4, 5, 6, 7, 9, 10]
def divible_by_5(n):
    if n%5==0:
        return n
    return False

num = list(filter(divible_by_5, l))
print(num)
