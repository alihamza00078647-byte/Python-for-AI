# def Number(i , n, num = 0):
#     if num == n:
#         return n
#     else:
#         i = i + 1
#         return i
    
# c= Number(i = 1, n = int(input("Enter the End Number: ")))
# print(c)
def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1) + n
    

print(sum(5))



