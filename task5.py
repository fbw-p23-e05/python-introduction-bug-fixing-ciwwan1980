# Your task is to fix program non-working correctly.
# The problem:  
#   - sum the three prompted integers
#   - however, if two values are equal sum should be zero
#   - calculate what result should be and what you get after running the program  

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z:
    result = 0
else:
    result = x + y + z

print("Calculated sum is", result)


