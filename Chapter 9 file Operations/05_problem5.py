list_of_words = ["WAQAS", "Ahmad", "Husnain"]

with open("file.txt", "r") as f:
    content = f.read()

for words in list_of_words:
    content_of_list = content.replace(words, "#"* len(words))



with open("file.txt", "w") as f:
    f.write(content_of_list)