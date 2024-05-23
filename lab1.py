"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Write a function named welcome_message that prints out "Welcome to our program!" whenever it is called.

def welcome_message():
    print("welcome to our program")


# Create a function named print_divider that prints out a line of asterisks (e.g., "**********") to act as a section divider.

def print_divider():
    print("***********")


# Write a function named get_number that asks the user to input a whole number and then returns the result as an integer.

def get_number():
    poo = input("enter a numberrrrrrr:")
    while not poo.isdigit():
        poo = input("enter a number")
    return int(poo)


# Create a function named get_random_colour that, when called, returns a random colour from a predefined list of colours.

def get_random_colour():
   a = print("red")
   b = print("blue")
   c = print("green")
   d = print("yellow")
   f = print("purple")
   g = print("pink")
    




# Call all of your functions to demonstrate that they work

welcome_message()
print_divider()
get_number()
get_random_colour()
