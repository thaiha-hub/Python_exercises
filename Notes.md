# Notes

### Leap year
Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400. 
Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

Answer1:

```python
year=int(input("Please type in a year:"))

if year%4==0:
    if year%100 != 0:
        print("That year is a leap year.")
    elif year%100 ==0 and year%400==0:
        print("That year is a leap year.")
    elif year%100 ==0 and year%400!=0:
        print("That year is not a leap year.")

else:
    print("That year is not a leap year.")

```
Answer2: 

```python
year = int(input("Please type in a year: "))
 
# First, we make assumption that a year is not a leap year
leap_year = False
 
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True
 
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
```
### Gift taxes
According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

When the gift is received from a close relative or a family member, the amount of tax to be paid is determined by the following table, which is also available on this website:

Value of gift	    Tax at the lower limit	    Tax rate for the exceeding part (%)
5 000 — 25 000	    100	                            8
25 000 — 55 000	    1700	                        10
55 000 — 200 000	4700	                        12
200 000 — 1 000 000	22100	                        15
1 000 000 —	        142100	                        17

My answer:
```python
vog = int(input("Value of gift: "))
x = int()
y = int()
z = int()
tax = 0

if vog >= 5000 and vog < 25000:
    x = 100
    y = 8
    z = 5000
elif vog >= 25000 and vog < 55000:
    x = 1700
    y = 10
    z = 25000
elif vog >= 55000 and vog < 200000:
    x = 4700
    y = 12
    z = 55000
elif vog >= 200000 and vog < 1000000:
    x = 22100
    y = 15
    z = 200000
elif vog >=1000000:
    x = 142100
    y = 17
    z = 1000000
else:
    print("No tax!")

tax = x + (vog - z) * y/100
if tax >0:
    print(f'Amount of tax: {tax}')
```
