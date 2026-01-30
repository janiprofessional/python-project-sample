def primeNumberList(num):
    list = []
    for i in range(2, num):
        for j in range(2,i):
            if i%j == 0:
                break
    
        else:
            list.append(i)
    print(list)

number = int(input("Enter the number for prime numbers list: "))
primeNumberList(number)

# output: 
# Enter the number for prime numbers list: 100
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
# 31, 37, 41, 43, 47, 53, 59, 61, 67, 
# 71, 73, 79, 83, 89, 97] 
# 
#


def primeOrNot(num):
    if num%2 == 0:
        print(f"given {num} number is not prime")
    else:
        print(f"given {num} number is prime")

num = int(input("Enter the number it is prime or not: "))
primeOrNot(num)

# output: 
# Enter the number it is prime or not: 4 
# given 4 no is not prime