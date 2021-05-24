a=int(input('enter amount'))
if (a>=1000 and a<2000):
    print('Total bill is',a)
    d=a*10/100
    print('Discount on the billed amount is ',d)
    bill=a-d
    print('paid bill :',bill)
else:
    if (a>=2000 and a<3000):
        print('Total bill is ',a)
        d=a*20/100
        print('Discount on the billed amount is',d)
        bill=a-d
        print('paid bill : 1600')
    elif(a>=3000 and a<5000):
        print('Total bill is',a)
        d=a*30/100
        print('Discount on the billed amount is ',d)
        bill=a-d
        print('paid bill :',bill)
    elif(a>=5000):
        print('Total bill is',a)
        d=a*40/100
        print('Discount on the billed amount is ',d)
        bill=a-d
        print('paid bill :',bill)
    
'''output
enter amount2200
Total bill is  2200
Discount on the billed amount is 440.0
paid bill : 1600'''
