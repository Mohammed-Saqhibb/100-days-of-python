## Day 6 Challenges & Solutions

### Challenge 1: Escape the Maze
**Problem:** Navigate from start to exit using functions and loops
**Solution:** 
- Create `move()` function for valid moves
- Use `while` loop for game continuation
- Check boundary conditions before moving

### Challenge 2: Validate User Input
**Problem:** Keep asking until valid input
**Solution:**
```python
def get_valid_direction():
    valid = ['up', 'down', 'left', 'right']
    while True:
        direction = input("Enter direction: ").lower()
        if direction in valid:
            return direction
```

### Challenge 3: Track Player Position
**Problem:** Keep track of current position in maze
**Solution:**
- Use tuple (x, y) for coordinates
- Pass to functions as parameters
- Return updated position

### Challenge 4: Check Win Condition
**Problem:** Determine when player reaches the exit
**Solution:**
- Compare current position with exit coordinates
- Break out of while loop when condition met
- Display victory message

### Lessons Learned
- Functions make code modular and testable
- While loops handle variable iteration counts
- Parameters are safer than global variables
- Return values keep functions pure
- Break statement is useful but needs careful placement
