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
        print(any(i.isalnum() for i in (s)))
        print(any(i.isalpha() for i in (s)))
        print(any(i.isdigit() for i in (s)))
        print(any(i.islower() for i in (s)))
        print(any(i.isupper() for i in (s)))
