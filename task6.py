
# Your task is to fix program non-working correctly.
# The problem:  
# - sum the two prompted integers
# - however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20  
# - calculate what result should be and what you get after running the program 

x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y
sum=0
if result > 15 and result < 20:
    sum = 20
else: 
    sum=result
print("Calculated sum is ", sum)