'''Ask the user for a string and print out whether this string is a palindrome or not'''

def isPalindrome(string):
    return string == string[::-1]
 
s = str(input("Enter a string: ")).upper()
ans = isPalindrome(s)
 
if ans:
    print("Yes,{} is a palindrome.".format(s))
else:
    print("No,{} is not a palindrome.".format(s))