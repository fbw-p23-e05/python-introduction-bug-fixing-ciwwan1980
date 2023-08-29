
# Your task is to fix program non-working correctly.
# The problem:  
# - prompt three float numbers and determine the largest and the smallest one
# - calculate what result should be and what you get after running the program

x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

max_value = max(x, y, z)
min_value = min(x, y, z)

print("The maximum value is", max_value)
print("The minimum value is", min_value)
