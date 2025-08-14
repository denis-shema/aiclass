# creating dictionary
contact_book = {"rose":"123456789","shema":"876543","john":"456789","mary":"6788765"}
contact_book["denis"]="0990569346"
contact_book["erick"]="345678"
contact_book["makumba"]="0883615693"

# accessing dictionary
print(contact_book["mary"])
print(contact_book["makumba"])

# updating dictionary
contact_book["erick"]="888888888"

# deleting item in dictionary
deleted_number = contact_book.pop("mary")
print(contact_book)

# menu for denis restaurant
menu={"pizza":"12.29","salad":"6.99","fish":"10.99"}
del menu["salad"]
print(menu)

# looping through dictionary
# loop through keys
for items in contact_book.keys():
    print(items)

#loop through values
for numbers in contact_book.values():
    print(numbers)

# loop through key values
for item, numbers in contact_book. :
    print(f"{item}:{numbers}")