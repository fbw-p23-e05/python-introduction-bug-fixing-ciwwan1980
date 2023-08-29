# Your task is to fix program non-working correctly.
# The problem:  
#   - sum integers from 1 to 5 using `range()` function
#   - calculate what result should be and what you get after running the program  

n = 5
sum = 0
for num in range(n+1):
    sum += num
print("Sum =", sum)