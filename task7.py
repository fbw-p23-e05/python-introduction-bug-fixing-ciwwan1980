# Your task is to fix program non-working correctly.
# The problem:  
# - prompt two values and assign them to variables `a` and `b`
# - write the Python program to swap these two variables
# - calculate what result should be and what you get after running the program   
# >Remark: **don't use** "fast" swapping available in Python: 


# First solution
# a = int(input("First value: "))
# b = int(input("Second value: "))


# print(f"before swapping a= {a} , b= {b}")

# temp = a
# a = b
# b = temp

# print("After swapping: a =", a, ", b =", b)

# Second solution

a = int(input("First value: "))
b = int(input("Second value: "))

print(f"before swapping a= {a} , b= {b}")

a, b = b, a  

print(f"after swapping a= {a} , b= {b}")
