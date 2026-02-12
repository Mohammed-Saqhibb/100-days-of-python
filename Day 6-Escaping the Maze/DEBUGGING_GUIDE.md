## Debugging Function and Loop Errors

### Common Function Bugs

**Bug 1: Missing Return Statement**
```python
# Wrong
def get_area(length, width):
    area = length * width  # Returns None!

# Correct
def get_area(length, width):
    return length * width
```

**Bug 2: Scope Issues**
```python
# Wrong
x = 5
def modify_x():
    x = 10  # Creates local x, doesn't modify global

# Correct
x = 5
def modify_x():
    global x
    x = 10
```

**Bug 3: Mutable Default Arguments**
```python
# Wrong
def append_item(item, lst=[]):
    lst.append(item)
    return lst

# Correct
def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### Common Loop Bugs

**Bug 1: Infinite Loop**
```python
# Wrong
x = 0
while x < 10:  # x never changes!
    print(x)

# Correct
x = 0
while x < 10:
    print(x)
    x += 1
```

**Bug 2: Off-by-One Error**
```python
# Wrong
for i in range(10):  # Goes 0-9, if you want 1-10
    print(i)

# Correct
for i in range(1, 11):  # Goes 1-10
    print(i)
```

**Bug 3: Break Inside Nested Loop**
```python
# Breaks inner loop, not outer
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
    print(i)  # Still executes
```

### Debugging Techniques
1. Use `print()` statements to track execution
2. Add comments to clarify logic
3. Test functions with edge cases
4. Use a debugger for complex issues
5. Break problems into smaller functions
