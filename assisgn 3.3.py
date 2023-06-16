numbers = input("Enter a list of numbers (space-separated): ").split()
sum_positive = 0

for number in numbers:
    number = int(number)
    
    if number < 0:
        continue
    
    sum_positive += number

print("Sum of positive numbers:", sum_positive)
