num = int(input("Enter a number to check for palindrome: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(f"{original} is a Palindrome Number")
else:
    print(f"{original} is NOT a Palindrome Number")
