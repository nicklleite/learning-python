# Section 03

# ##############################################################################
# Coding challenge part 2.
#
# - Create a list of your favorite food items, the list should have minimum
#   five elements.
# - List out the 3rd element in the list.
# - Add additional item to the current list and display the list.
# - Insert an element named tacos at the 3rd index position of the list and
#   print out the list elements.
# ##############################################################################

favorite_foods = [
    'Strogonoff',
    'Frango empanado',
    'Risoto',
    'Macarrão',
    'Bolo de carne'
]

print(favorite_foods[3])

favorite_foods.append('Torta de frango')

favorite_foods.insert(3, 'Doguinho')

print(favorite_foods)

# ##############################################################################
# Coding challenge part 3
#
# - Task no 1: Using a for-loop and a range function, print "I am a programmer"
#   5 times.
# - Task no 2: Create a function which displays out the square values of
#   numbers from 1 to 9.
# ##############################################################################

# Task 01
for x in range(0, 5):
    print("I am a programmer")

# Task 02
for x in range(1, 10):
    print(x**2)
