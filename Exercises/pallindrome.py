#Check if the given string is a pallindrome or not
def pallindrome(pallindrome):
    a = str(pallindrome).lower()
    b = a[::-1].lower()
    if a == b:
        print(f'{pallindrome} is a Pallindrome')
    else:
        print(f'{pallindrome} is not a Pallindrome')

print(pallindrome("Nissin"))