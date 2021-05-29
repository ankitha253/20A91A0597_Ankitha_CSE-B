#To find reverse of a number using while loop.
num=int(input())
rev=0
while(num>0):
    reminder=num%10
    rev=(rev*10)+reminder
    num=num//10
print('reversed number is %d'%rev)

'''expected output
13579
reversed number is 97531'''

'''actual output
13579
reversed number is 97531'''
