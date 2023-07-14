# Program to check whether the given input is an alphabet, digit or a special character

character = input()
asci = ord(character)

"""
NOTE: When we come across if elif statements, only the body of the first true condition gets executed.
If there are multiple if statements, then all the conditions that hold true will get executed.
"""

if asci>=65 and asci<=90:
    print("Upper")
    
#Alternate statements (Nested if)
#if asci>=65:
#    if asci<=90:
#        print("Upper")



#print("Hello") #Error: We cannot enter any other lines of code in between the if else structure other than their body

elif 97<=asci<=122:
    print("Lower")
elif 48<=asci<=57:
    print("Number")
else:
    print("Special character")