spam = "make a lot of money"
spam1 = "buy now" 
spam2 = 'subscribe this'
spam3 = 'click this'
message = input("Enter Your Comment: ")
if (spam in message) or (spam2 in message) or ( spam3 in message) or (spam1 in message):
    print("Its a Spam")
else:
    print(message)