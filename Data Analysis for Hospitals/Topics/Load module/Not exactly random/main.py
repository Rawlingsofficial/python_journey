# place `import` statement at top of the program
import random

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here

random.seed(n)
random_number = random.randint(-100, 100)
print(random_number)