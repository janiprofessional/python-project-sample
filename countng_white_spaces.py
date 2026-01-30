# using count method
text = "Hi Python Program"
count = text.count(" ")
print("Number of count spaces are:",count)
# output : Number of count spaces are: 2

# count using loop
count = 0
for char in text:
    if char == " ":
        count += 1
print("spaces count through looping are ",count)
# output: spaces count through looping are  2

# counting with method
def space_count(text):
    count = text.count(" ")
    return count
str = "Hi Hello How are you"
print("Total space counts are:",space_count(str))
# output : Total space counts are: 4

str = "Hello this is 123 @#$"
letter = 0
digit = 0
spaces = 0
spe_char = 0
for char in str:
    if char.isalpha():
        letter +=1
    elif char.isdigit():
        digit +=1
    elif char.isspace():
        spaces +=1
    elif not char.isalnum() and not char.isspace():
        spe_char +=1

print("letters are:",letter)
print("digits are:",digit)
print("spaces are:",spaces)
print("specials chars are:",spe_char)

# putput
# letters are: 11
# digits are: 3
# spaces are: 3
# specials chars are: 3