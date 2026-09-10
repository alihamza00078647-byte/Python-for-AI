a = {
    "marks" : 90,
    "Ali" : 98,
    "Hamza" : 20
}

# print(a.get("Ali2"))    #Prints None
# print(a['Ali2'])    #Through an error
# a.clear()
value = a.pop('marks')
print(value)
