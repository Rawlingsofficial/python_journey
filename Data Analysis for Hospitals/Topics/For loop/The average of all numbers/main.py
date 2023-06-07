# put your python code here
a = int(input())
b = int(input())

sum_of_divisible = 0
count = 0

for num in range(a, b+1):
    if num % 3 == 0:
        sum_of_divisible += num
        count += 1

mean = sum_of_divisible / count
print(mean)
