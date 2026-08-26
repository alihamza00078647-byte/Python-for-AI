letter = '''         Dear <|Name|>,        
    You are selected!        
    <|Date|> '''

print(letter.replace("<|Name|>", "ALi").replace("<|Date|>", "09/12/2020"))
# print(letter.replace("<|Date|>", "09/12/2024"))

# print(letter)