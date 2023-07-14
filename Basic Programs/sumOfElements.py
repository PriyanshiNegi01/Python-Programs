# Python program to take n numbers and print the same along with their sum

sum=0
num = []

n = int(input("Enter the total number of elements: "))
for i in range(1, n + 1):
    value = int(input("Enter the element %d: " %i))
    num.append(value)

#total = sum(NumList)
for i in range(n):
    sum=sum+num[i]

print("You have entered:")

for i in range(n):
    print(num[i])

print("\nSum of all the elements is: ", sum)
