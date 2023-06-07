string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0

for char in string:
    if char.lower() in vowels:
        count += 1

print("Number of vowels:", count)
