## Assignment 1: List Basics Practice (15 minutes)

### Instructions
Create a file called `assignment1_list_basics.py` and complete the following tasks:

1. **Create Lists**
   - Create a list of your 5 favorite movies
   - Create a list of 5 random numbers
   - Create an empty list for storing user input

2. **Access and Modify**
   - Print the first and last movie from your list
   - Change the third number in your numbers list
   - Add two more movies to your favorites list

3. **List Operations**
   - Print the total number of movies
   - Remove one movie from the list
   - Check if a specific number exists in your numbers list

### Example Output
```
My favorite movies: ['Inception', 'The Matrix', 'Interstellar', 'Avatar', 'Dune']
First movie: Inception
Last movie: Dune

Numbers before: [7, 23, 45, 12, 89]
Numbers after changing third: [7, 23, 100, 12, 89]

Total movies: 5
After adding movies: ['Inception', 'The Matrix', 'Interstellar', 'Avatar', 'Dune', 'Spider-Man', 'Iron Man']
After removing: ['Inception', 'Interstellar', 'Avatar', 'Dune', 'Spider-Man', 'Iron Man']

Is 45 in the list? False
```

## Assignment 2: Basic Function Practice (15 minutes)

### Instructions
Create a file called `assignment1_basic_functions.py` and complete the following tasks:

1. **Simple Functions**
   - Create a function that greets a person by name
   - Create a function that calculates the area of a rectangle
   - Create a function that converts Celsius to Fahrenheit

2. **Functions with Default Parameters**
   - Create a function that introduces a person with optional title
   - Create a function that calculates compound interest with default values
   - Create a function that formats a phone number with optional country code

3. **Return Values**
   - Create a function that returns both quotient and remainder of division
   - Create a function that returns multiple statistics about a number list
   - Create a function that validates and returns formatted user input

### Example Output
```
=== Greeting Functions ===
Hello, Alice!
Hello, Dr. Smith!

=== Area Calculator ===
Rectangle area (5x3): 15

=== Temperature Converter ===
25°C = 77.0°F

=== Division Results ===
10 ÷ 3 = 3 remainder 1

=== List Stats ===
Numbers: [1, 2, 3, 4, 5]
Sum: 15, Average: 3.0, Count: 5
```

## Assignment 3: Personal Calculator (10 minutes)

### 🎯 **Objective**
Create a personal calculator with functions for basic operations that uses different parameter types.

### 📋 **Requirements**
1. Create functions for `add`, `subtract`, `multiply`, and `divide`
2. Add an optional `precision` parameter (default: 2 decimal places)
3. Test all functions with different parameter combinations
4. Use both positional and keyword arguments in your tests

### 💻 **Template**
```python
def add(num1, num2, precision=2):
    """Add two numbers with optional precision"""
    # Your code here
    pass

def subtract(num1, num2, precision=2):
    """Subtract two numbers with optional precision"""
    # Your code here
    pass

def multiply(num1, num2, precision=2):
    """Multiply two numbers with optional precision"""
    # Your code here
    pass

def divide(num1, num2, precision=2):
    """Divide two numbers with optional precision"""
    # Your code here
    pass

# Test your functions here with different approaches:
# - Using default precision
# - Using positional precision argument
# - Using keyword precision argument
```

### ✅ **Example Output**
```
Testing add function:
8.67 (using default precision)
8.7 (using positional precision=1)
9 (using keyword precision=0)
```

### 🔍 **What You're Learning**
- Function definition syntax
- Required vs optional parameters
- Different ways to call functions (positional vs keyword arguments)
- Using return values

---
