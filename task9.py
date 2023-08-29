

# Your task is to fix program non-working correctly.
# The problem:  
# - prompt value from the user and assign it to some variable  
# - if given value is 0 (zero) convert it to `False` and if given value is 1 convert it to `True`
# - display results  

x = input("Type your value: ")

if x == "0":
    x = False
elif x == "1":
    x = True

print("Your entered value is now", x)

