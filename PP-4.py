

'''If-Else
if condition:   #True
      statment(s)
else:       #False
    statment(s)
TO read the age of student and
check whether student is eligible for vote or not:'''
 
name=input("Enter input")
age=int(input("Enter age"))
if age<=18:
      print("SORRY!",name)
      print("The person is NOT ELIGIBLE for Vote")
else:
      print ("HELLO",name)
      print ("The person is ELIGIBLE for vote due to")


 '''EXPECTED OUTPUT     
Enter inputsujuika
Enter age19
SORRY! sujuika
The person is NOT ELIGIBLE for Vote'''

'''ORIGINAL OUTPUT
Enter inputsujuika
Enter age19
SORRY! sujuika
The person is NOT ELIGIBLE for Vote'''

'''EXPECTED OUTPUT
Enter input LUCKY
Enter age 7
SORRY! LUCKY
The person is NOT ELIGIBLE for Vote'''

'''ORIGINAL OUTPUT
Enter input LUCKY
Enter age 7
SORRY! LUCKY
The person is NOT ELIGIBLE for Vote'''
