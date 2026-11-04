"""
1 = "Snake"
-1 = "Gun"
0 = "Water"

"""
l = [1, -1 , 0]
import random
computer_choice = random.choice(l)
# print("Compter's Choice is ", computer_choice)


# computer_choice = int(input("Enter Computer's Choice: "))

user_choice = int(input("Enter Your Choice: "))

if computer_choice == user_choice:
    print("Its a Draw")

else:
    if (computer_choice == 1 and user_choice == -1):
        print(f"Your choice is {user_choice} and Computer's choice is {computer_choice}")
        print("You WON")
    elif (computer_choice == 0 and user_choice == 1):
        print(f"Your choice is {user_choice} and Computer's choice is {computer_choice}")
        print("You Won")
    elif (computer_choice == -1 and user_choice == 1):
        print(f"Your choice is {user_choice} and Computer's choice is {computer_choice}")
        print("You Lose!")
    elif (computer_choice == 1 and user_choice == 0):
        print(f"Your choice is {user_choice} and Computer's choice is {computer_choice}")
        print("You Lose!")
    elif (not user_choice == 1 or -1 or 0):
        print("Invalid Input, Please Enter the Right Choice")
