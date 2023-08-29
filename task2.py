# ### :heavy_plus_sign: Task 2 - summing integers

# Your task is to fix program non-working correctly.
# The problem:  
#   - sum integers from 1 to 5 using while loop
#   - calculate what result should be and what you get after running the program   

n = 5
number = 1
sum = 0
while number <= n:
    print(number)
    sum += number
    number  +=1 
print("Sum =", sum)