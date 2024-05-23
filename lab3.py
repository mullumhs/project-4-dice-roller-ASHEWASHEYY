"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to use exception handling in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Define a function called get_number(prompt) that returns an integer. 
# Include a while loop and try/except blocks inside the function to handle non-integer inputs.

def get_number():
    while True:
        try:
            num = int(input("enter a numba:"))
            return num
        except:
            print("wrong bozo get gud")

# Use the get_number function to ask for a numerator, then again for a denominator.
# Divide the numerator by the denominator and print the result, handling any division by zero errors.
numerator = get_number()
denominator = get_number
while True:
    try:
        result = numerator / denominator
        break
    except:
        print("LOSER NAW")
        denominator = get_number()
print(result)

# Use the get_number function to ask the user for an index to access an element from a predefined list. 
# Print out the value from the list, handling the index error if the user selects a non-existent index.