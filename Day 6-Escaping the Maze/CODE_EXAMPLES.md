## Function Examples from Day 6

### Example 1: Simple Function
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### Example 2: Function with Return
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### Example 3: While Loop with Function
```python
def validate_input():
    while True:
        user_input = input("Enter a number: ")
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input, try again")

num = validate_input()
```

### Example 4: Maze Navigation Function
```python
def move_in_maze(current_pos, direction):
    x, y = current_pos
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    # ... more directions
    return (x, y)
```

### Best Practices
1. Keep functions small and focused
2. Use meaningful function names
3. Add docstrings for complex functions
4. Avoid modifying global variables inside functions
5. Use parameters instead of accessing external variables
