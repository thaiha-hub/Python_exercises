# PYTHON LOOPS

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

### Loop nr3
Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

Answer:
```python
attempt = 0

while True:
    number = int(input("PIN: "))
    if number != 4321:
        attempt +=1
        print("Wrong")
    elif number == 4321:
        attempt +=1
        break

if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f'Correct! It took you {attempt} attempts')
```

## while True:
**"Keep doing this forever until I tell you to stop!"**
while True is an indefinite loop that one needs to break in order to stop it.

```python
while True:
    do_something()
    if something_is_true:
        break  # 🛑 Exit the loop
```
### Example: print out the next leap year when inputting a random year

```python
year = int(input("Year:"))
l_year = year+1

while True:
    if l_year%4 == 0 and l_year % 100 !=0:
        break
    elif l_year%4 ==0 and l_year%100 ==0 and l_year%400==0:
        break
    
    l_year +=1

print(f'The next leap year after {year} is {l_year}')
```
### Make a story: 
The loop will end when type in "end" or the same word twice. 

```python
prev_word=""
word = ""
text=" "

while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    
    elif word == prev_word:
        break
        
    text += word + " "
    prev_word = word
    
print (text)
```
### Working with numbers

```python
number=int()
count= 0
total =int()
neg_count=0
pos_count=0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))
    count +=1
    total +=number

    if number>0:
        pos_count +=1
    if number < 0:
        neg_count +=1

    if number == 0:
        break
    if (count) !=0:
        meen = total/ (count)

print(f'Numbers typed in {count-1}')
print("The sum of the numbers is", total)
print("The mean of the numbers is", meen)
print("Positive numbers", pos_count)
print("Negative numbers", neg_count)
```

