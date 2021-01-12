string = input("Give me a palindrome (or not): ")

str_rev = string[::-1]

if (string == str_rev):
    print("it's a palindrome.")
else:
    print("it's NOT a palindrome.")
