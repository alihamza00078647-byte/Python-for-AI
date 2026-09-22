def star_pattern(n):
    if n==0:
        return
    print("*" *n)
    star_pattern(n-1)


print(star_pattern(5))