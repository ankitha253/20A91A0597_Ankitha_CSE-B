a=int(input('The base is: '))
b=int(input('The power is: '))
x=pow(a,b)
rem=x%10
print('The value of %d^%d is %d'%(a,b,x))
print('The last digit of %d is %d '%(x,rem))

'''output
The base is: 4
The power is: 4
The value of 4^4 is 256
The last digit of 256 is 6 '''
