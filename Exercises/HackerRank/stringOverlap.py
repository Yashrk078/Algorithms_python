'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.
'''
string = "ABCDCDCDC"
sub_string = "CDC"
if 1 <= len(string) <= 200:
    count =0  
    while string.find(sub_string) != -1:
        pos, count = string.find(sub_string), count+1
        string = string[pos+1:]
    print(count)
    