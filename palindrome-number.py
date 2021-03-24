x = -121
def palindrome(x):
    str_x = str(x)
    if(str_x[:]==str_x[::-1]):
        return 'true'
    else:
        return 'false'
print(palindrome(x))