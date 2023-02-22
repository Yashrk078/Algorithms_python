'''
https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
'''
# width=20
# print('Test'.ljust(width,'-'))
# print('Test'.center(width,'-'))
# print('Test'.rjust(width,'-'))
thickness = int(input()) #This must be an odd number
c = 'H'
if 0 < thickness < 50:
    if not ((thickness % 2) == 0): 
        #Top Cone
        for i in range(thickness):
            print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

        #Top Pillars
        for i in range(thickness+1):
            print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

        #Middle Belt
        for i in range((thickness+1)//2):
            print((c*thickness*5).center(thickness*6))    

        #Bottom Pillars
        for i in range(thickness+1):
            print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

        #Bottom Cone
        for i in range(thickness):
            print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))