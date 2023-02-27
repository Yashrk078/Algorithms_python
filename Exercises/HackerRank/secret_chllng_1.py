#Return max number of count of substring occurences
def solution(s):

    length_of_str = len(s)

    for i in range(1,length_of_str+1):

        cmp_str = s[:i]

        count = s.count(cmp_str)

        if count*i == length_of_str:
            return count
print(solution('abcabc'))

#another soln
# return max([s.count(s[:x]) for x in xrange(len(s)) if s[:x]*s.count(s[:x]) == s])


#another:
# def solution(s):
#     # res = None
#     # for i in range(1, len(s)//2 +1 ):
#     #     if (not len(s)%len(s[0:i])) and (s[0:i]) * (len(s)//len(s[0:i])) == s:
#     #         res = s[0:i]
#     return max([s.count(s[:x]) for x in xrange(len(s)) if s[:x]*s.count(s[:x]) == s])

# inputstr = str(raw_input())
# print solution(inputstr)