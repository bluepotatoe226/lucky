with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()
lowercase = 0
uppercase = 0
digits = 0

for char in data:
    if char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    elif char.isdigit():
        digits += 1

print(f"The lowercase count is: {lowercase} letters")
print(f"The uppercase count is: {uppercase} letters")
print(f"The digit count is: {digits} digits")

