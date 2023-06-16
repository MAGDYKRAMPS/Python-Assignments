sum_positive = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    
    sum_positive += number

print("Sum of positive numbers:", sum_positive)
