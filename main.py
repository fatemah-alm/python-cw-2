# write your code here
#first part
my_name = input("Enter your name: ")
my_age = input("Enter your age: ")

print(f"My name is {my_name} and i am {my_age} years old")

#second part
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation: ")

if operation not in ["+", "-", "*", "/"]:
    print("Operation is not valid")
elif operation == "+":
    print(f"the result is {first_number + second_number}") 
elif operation == "-":
    print(f"the result is {first_number - second_number}") 
elif operation == "*":
    print(f"the result is {first_number * second_number}") 
elif operation == "/":
    print(f"the result is {first_number / second_number}") 


#third part

number = input("Choose a number between 1 & 12: \n")
plural = input("Enter a plural noun: \n")
name = input("Enter your name: \n")
sentence = input("Enter any sentence: \n")
verb = input("Enter any verb: \n")

print(f"""
The story goes...
It was {number} o'clock when I heard a knock at the door.
I opened the door and there was a box full of {plural} with a note saying From {name}.
Just as I closed the door I heard a scream {sentence}
I froze in place and all I could do was {verb}.
""")

