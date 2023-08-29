# Your :heavy_plus_sign: Task is to fix program non-working correctly.
# The FizzBuzz problem:  
# For all integers between 1 and 99 (include both):  
# - print 'fizz' for multiples of 3,
# - print 'buzz' for multiples of 5, 
# - print 'fizzbuzz' for multiples of 3 and 5.

three_mul = "fizz"
five_mul = 'buzz'
num1 = 3
num2 = 5 
max_num = 100
   
for i in range(1,max_num+1):
    
    # first condition shall include both num and num2,  otherwise , if i put the order not like this, it will never go to this condition, because it will always be true  
    if (i%num1 == 0 and i%num2 == 0):
        print(i, three_mul+five_mul) 

    elif i%num2 == 0:
        print(i, five_mul)
    elif  i %num1 == 0:
        print(i, three_mul)   