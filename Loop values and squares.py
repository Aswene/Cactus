#To design and implement a Python application that prints all numbers
#between 1 and 100 with the square value in the allotted time specified.

#1.Create a Python application that will loop between 1 and 100.
for i in range (1,101):
    print(i)

#2.The numbers are to be printed out alongside their squared value.
for i in range (1,101):
    s = i**2
    print(i,s)

#3.The app should stop when a squared value of 200 or more is reached.
for i in range (1,101):
    s = i**2
    if int(s)<200:
        print(i,s)

#4.Reconfigure the application to take in a user value to produce squared values up to..
x = int(input('Enter max value to be squared:'))
for i in range (1,x+1):
    s = i**2
    if int(s)<200:
        print(i,s)
