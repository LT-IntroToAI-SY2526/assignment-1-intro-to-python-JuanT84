# Assignment 1: AI-Generated Python Problems
# Name: [Juan Torres]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[Paste the prompt you used to generate your problem set here]

"I'm learning Python basics in a high school programming class. I'm new to programming. Can you create 5-7 practice problems that cover:
> - Variables and basic data types
> - Conditionals (if/elif/else)
> - Loops (for and while)
> - Functions
> - Basic list operations
> 
> Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

"""Problem 1: Favorite Number (Variables & Data Types)

Objective: Practice using variables and basic data types.

Instructions:
Write a program that stores your name and your favorite number in variables. Then, print a message like:

"Hello, my name is Alex and my favorite number is 7."


Example Output:

Hello, my name is Jamie and my favorite number is 12."""

name_str = input("Please enter your name: ")
num_int = int(input("Please enter your favorite number "))
print(f"Hi my name is {name_str} my favorite number is {num_int}")



"""Problem 2: Movie Ticket Price (Conditionals)

Objective: Use if, elif, and else statements.

Instructions:
Write a program that asks for a person's age and prints the cost of a movie ticket based on the following rules:

Under 5 years old: Free

5 to 12 years old: $5

13 to 59 years old: $10

60 and older: $7

Example Input/Output:

Enter your age: 3
Ticket price: Free

Enter your age: 10
Ticket price: $5

Enter your age: 70
Ticket price: $7"""

age = int(input("Please Input Your Age "))
if age < 5:
    print("Ticket Price: Free")
elif age <=12:
    print("Ticket Price: $5")
elif age <=59:
    print("Ticket Price: $10")
else:
    print("Ticket Price: $7")


"""Problem 3: Count to Ten (Loops)

Objective: Use a while loop and a for loop.

Instructions:
Write two separate loops that count from 1 to 10 (inclusive).

First, use a while loop.

Then, use a for loop.

Example Output:

Using while loop:
1 2 3 4 5 6 7 8 9 10

Using for loop:
1 2 3 4 5 6 7 8 9 10"""

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()
for i in range (1, 11):
  print(i, end=" ")
  

  """Problem 4: Even or Odd Checker (Functions + Conditionals)

Objective: Write and use a function.

Instructions:
Create a function called check_even_or_odd(number) that takes a number as input and prints whether it is even or odd.

Then, ask the user for a number, pass it to the function, and show the result.

Example Input/Output:

Enter a number: 9
9 is odd

Enter a number: 4
4 is even"""

num = int(input("Enter a Number"))
def check_even_or_odd(num):
    check = num % 2 
    if check == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
check_even_or_odd(num)

"""Problem 5: List Analyzer (Lists + Loops + Functions)

Objective: Work with lists and loop through them in a function.

Instructions:
Write a function called analyze_numbers(numbers) that:

Takes a list of numbers as input

Prints the largest number

Prints the smallest number

Calculates and prints the average of the numbers

Example Input/Output:

numbers = [10, 5, 8, 20, 3]
analyze_numbers(numbers)


Output:

Largest number: 20
Smallest number: 3
Average: 9.2"""

num = [10,5,8,20,3]
def analyze_numbers(num):
    largest = max(num)
    minimum = min(num)
    average =  sum(num)/len(num)
    print(f"Largest Number: {largest}")
    print(f"Smallest Number: {minimum}")
    print(f"Average Number: {average}")
analyze_numbers(num)









# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
"""
"""Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here



print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


