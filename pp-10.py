
#To read start,end,step_count values from user.
#By using while loop.
start=int(input('starting value'))
end=int(input('ending value'))
step_count=int(input('step_count'))
while start<=end:
    print (start)
    start+=step_count

'''expected output    
starting value1
ending value20
step_count2
1
3
5
7
9
11
13
15
17
19'''

'''original output
starting value1
ending value20
step_count2
1
3
5
7
9
11
13
15
17
19'''
