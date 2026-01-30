numberList=[12,3,55,23,6,78,33,4]
# find the max number in list with max() & min ()
#print(max(numberList))
#print(min(numberList))

max=numberList[0]
min=numberList[0]
for number in numberList:
    if (number > max):
        max = number
print("Maximum number is: ",max)

for number in numberList:
    if(number < min):
        min = number
print("Minimum number is: ",min)


# Maximum number is:  78
# Minimum number is:  3