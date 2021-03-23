# Dictionaries

people = {
    "John": 32,
    "Rob": 23
}

# print(people["John"])

###############################################################################

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

# Check if the key is present on the dictionary
# print(1 in numbers)
# print(numbers.get(5, "Key not found!"))


###############################################################################

# Lists are mutable
# Tuples aren't

fruits = ("Apple", "Mango", "Peach")
# print(fruits)
# print(fruits[0])


###############################################################################

numbers = [0, 100, 200, 300, 400, 500, 600]
# print(numbers[2:6]) # Slice a part of the list

# Get all the items from the beginning of the list to the given index
# print(numbers[:3])

# Get all the items from the given index to the end of the list
# print(numbers[3:])

# Slice a part of the list with an interval between the indexes
# print(numbers[1:6:3])


###############################################################################

numbers = [x**2 for x in range(11) if x % 2 == 0]
# print(numbers)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


###############################################################################

numbers = [4, 5, 6]
newstring = "Numbers: {0}, {1}, {2}".format(numbers[0], numbers[1], numbers[2])
# print(newstring)

a = "{x}/{y}".format(x=100, y=200)
# print(a)


###############################################################################

# print(",".join(["Apple", "Banana", "Mango"]))

# newstring = "Hello There"
# print(newstring.replace("There", "World"))

# newstring = "This is a string"
# print(newstring.startswith("There"))

# newstring = "This is a string"
# print(newstring.endswith("There"))

# newstring = "This is a string"
# print(newstring.upper())
#
# newstring = "This is a string"
# print(newstring.lower())


###############################################################################

# print(max(1, 2, 3, 4, 5, 6))

# print(min(1, 2, 3, 4, 5, 6))

# print(abs(-203))


###############################################################################

###############################################################################
# Coding challenge part 7
#
# Write Python code which accepts name of a product and in turn returns their
# respective prices.
#
# Make sure to use dictionaries to store products and their respective prices.
#
# The dictionary should include at least 5 elements.
###############################################################################

# products = {
#     "Apple": 2.69,
#     "Banana": 0.69,
#     "Mushroom": 6.90
# }

# product_name = input("Enter the product name: ")
# print(products.get(product_name, "Product not found!"))


###############################################################################
# Coding challenge part 8
#
# List out  all the odd numbers from 1 to 100 using lists in Python.
###############################################################################

# print([x for x in range(1, 100) if x % 2 != 0])
