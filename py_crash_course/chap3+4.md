# LISTS

## Add items to the list
```python
list = [item1, item2, item3]
list.append(item4)
print(list) ---> [item1, item2, item3, item4]
list.insert(2, item5)
# [item1, item2, item5, item3, item4]
```
## Remove items from the list
```python
del list[o]              # when the item is removed by del function, one can no longer get it back. 
# --> [item2, item5, item3, item4]
list.pop(0)              # pop an item from any position of the list
print(list)              # [item5, item3, item4]
list.remove('item3')      # [item5, item4] remove function used when we know the item name 
```
## Organizing
```python
list.sort()
list.reverse()
```
## length of the list
len(list)
## Loops in The list
for list_item in list      

# NUMERICAL LISTS
## Using the range function  
**For loops**
```python
for value in range(1,6):
print(value)
```
**Make a list**
```python
numbers = list(range(1,5))
print(numbers)
# Result: [1, 2, 3, 4]
numbers = list(range(2, 11, 2)
# Result: [2, 4, 6, 8, 10]
