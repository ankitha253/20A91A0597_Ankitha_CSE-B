#Nested if:
username=input()
password=input()
if username=='CSEB':
      if password=='AEC':
          print ("valid student")
      else:
          print ("invalid password")
else:
    print("invalid username")

'''EXPECTED OUTPUT
CSEB
AEC
valid student

CSEB
aec
invalid password'''

'''ACTUAL OUTPUT
CSEB
AEC
valid student

CSEB
aec
invalid password'''
