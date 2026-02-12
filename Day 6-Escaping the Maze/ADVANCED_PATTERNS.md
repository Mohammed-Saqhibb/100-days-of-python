## Advanced Function Patterns

### Pattern 1: Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

### Pattern 2: Variable Arguments
```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```

### Pattern 3: Keyword Arguments
```python
def create_profile(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}
```

### Pattern 4: Return Multiple Values
```python
def divide_and_remainder(a, b):
    return a // b, a % b

quotient, remainder = divide_and_remainder(17, 5)
```

### Pattern 5: Nested Functions
```python
def outer(x):
    def inner(y):
        return x + y
    return inner
```

### Loop Control Patterns

#### Break Pattern
```python
while True:
    user_input = input("Quit? (yes/no): ")
    if user_input.lower() == "yes":
        break
```

#### Continue Pattern
```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

#### While-Else Pattern
```python
count = 0
while count < 5:
    count += 1
else:
    print("Loop completed normally")
```

### Performance Tips
- Use functions to avoid code duplication
- Reduce function call overhead with large computations
- Use appropriate loop type for the task
