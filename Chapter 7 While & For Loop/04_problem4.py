prime_number = int(input("Enter a Number: "))

for i in range(2, prime_number):
    if prime_number%i == 0:
        print(f"{prime_number} is NOt Prime Number")
        break
else:
    print(f"{prime_number} is Prime Number")