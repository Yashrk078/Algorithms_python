if __name__ == '__main__':
    s = input()
    #if 0 < len(s) < 100
    #if s.isalnum: True ? False
    #if s.aplha : True ? False
    #if s.isdigit : True ? False
    #if s.islower: True ? False
    #if s.isupper: True ? False

#the python any() function returns True if the iterable returns value as true, else False

    if 0 < len(s) < 100:
        print(any(s.isalnum() for s in s))
        print(any(s.isalpha() for s in s))
        print(any(s.isdigit() for s in s))
        print(any(s.islower() for s in s))
        print(any(s.isupper() for s in s))
