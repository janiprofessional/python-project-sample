# With out method
str1 = "listen"
str2 = "silent"

str1 = str1.replace(" ","").lower()
str2 = str2.replace(" ","").lower()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")


# output 
# True


# with Method
def is_Anagram(val1, val2):
    val1 = val1.replace(" ","").lower()
    val2 = val2.replace(" ","").lower()
    return sorted(val1) == sorted(val2)

print(is_Anagram("care", "race"))
print(is_Anagram("part","trap"))

#output: True 
# True
# output False incase of "car", "race"
