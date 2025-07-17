# LOOPS

## Simple loops

### Loop1

Please write a program which asks the user for integer numbers.
  If the number is below zero, the program should print out the message "Invalid number".
  If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
  In either case, the program should then ask for another number.
  If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

Answer:
```python
from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    if number < 0: 
        print("Invalid number")
    elif number > 0:
        print(sqrt(number))
    elif number == 0:
        print("Exiting...")
        break
```
### Loop2
Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

Answer:
```python
pass1 = input("Password: ")

while True:
    pass2 = input("Repeat password: ")
    if pass1 != pass2:
        print("They do not match!")
    elif pass1 == pass2:
        print("User account created!")
        break
```
