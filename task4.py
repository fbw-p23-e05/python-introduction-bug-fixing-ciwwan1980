# Your task is to fix program non-working correctly.
# The problem:  
#   - there are 4 short programs with loops, that should print some numbers, but they don't work at all!  

#- 1
for x in range(3):
    print(x)

#- 2

for j in range(5):
    print(f"This is loop number {j}")

#- 3

x=10
while x > 0:
    print(x)
    x -= 1
    
x = 10

# -4

countdown=5
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")