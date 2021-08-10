#Python program to check given string is Palindrome or not

def isPalindrome(s):

    return s == s[::-1]

s = "MADAM"
result = isPalindrome(s)
if result:
    print("Yes. Given string is Palindrome")
else:
    print("No. Given string is not Palindrome")
