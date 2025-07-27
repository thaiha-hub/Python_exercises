# LOOPS
for i in range()
## Arguments for range()

* for i in range(5) --> i can start from 0 or 1 till 5
* for i in range(4,10) --> i starts from 4 to 9 (up to 10 but not including 10)
* for i in range(0, 10, 2)

## Import modules
all python programs can call a basic set of functions called built-in functions/.  
python has also a set of modules called Standard library

### module sys.exit()
Ending the program early with sys.exit()

```python
import sys

while True:
    print('Type exit to exit.')
    response = input("Input: ")
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```
sys.exit() instantly stops the whole program 

**Difference btw break and sys.exit():**  
- Break only stops the loop
- sys.exit() stops the whole program. 
