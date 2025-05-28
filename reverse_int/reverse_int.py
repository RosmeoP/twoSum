number = int(input("Enter a number: "))

original = number
reverse = 0

if number < 0:
    print("Negative numbers can't be palindromes!")
else:
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        print(f"{original} is a palindrome!")
    else:
        print(f"{original} is NOT a palindrome!")
