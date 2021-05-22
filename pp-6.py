no=int(input())#input from STDIN
if no%2==0:
      print('Divisible by 2')
elif no%3==0:#15 --condition is true
     print('Divisible by 3')
elif no%4==0:
     print('Divisible by 4')
elif no%5==0:
     print('Divisible by 5')
else:
      print('Number is not divisible by 2,3,4,5')

'''Output
case 1:
40
Divisible by 2
Case2:
15
Divisible by 3
25
Divisible by 5
73
Number is not divisible by 2,3,4,5
'''

