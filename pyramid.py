def pyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(" ", end = "")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*", end= "")
        print("")


pyramid(5)


# output
#
#     *
#    ***
#   *****
#  *******
# *********
#

# shortcut code for pyramid
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# output was same above

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# output
#    1
#   1 2
#  1 2 3
# 1 2 3 4
#1 2 3 4 5
#