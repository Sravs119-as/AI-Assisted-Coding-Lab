# Take number input from user (dynamic way)
num = int(input("Enter a number: "))
# Initialize reverse number
reverse_num = 0
# Start a while loop to reverse digits
while num > 0:
    digit = num % 10           # Get the last digit
    reverse_num = reverse_num * 10 + digit  # Append digit to reversed number
    num = num // 10            # Remove last digit from num
print("Reversed number:", reverse_num)