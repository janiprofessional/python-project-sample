# Fibonacci series with method
def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b) 
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c <= 100:
                print(c)
            


fibonacci(100)

#output: 0
# 1
# 1
# 2
# 3
# 5
# 8 
# 13
# 21
# 34
# 55
# 89