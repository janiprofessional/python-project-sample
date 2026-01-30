# with out method
text = "madam"
palindromeText = text[::-1]

if text == palindromeText:
    print(F"{text} is palindrome")
else:
    print(f"{text} is not palindrome")

# with method

def is_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is Palindrome")
    else:
        print(f"{text} is not Palindrome")

print(is_palindrome("noon"))
print(is_palindrome(str(1213)))