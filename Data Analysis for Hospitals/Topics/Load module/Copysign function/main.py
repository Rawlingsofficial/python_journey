# place `import` statement at top of the program
import math
import math as m

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
m = math.copysign(x, y)
print(m)