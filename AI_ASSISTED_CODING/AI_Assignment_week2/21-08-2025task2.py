# Program to calculate the sum of even numbers in a list entered by the user

# take input from the user as a list of integers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_sum = 0

# iterate through the list
for num in numbers:
    if num % 2 == 0:   # check if even
        even_sum += num

print("Sum of even numbers:", even_sum)
