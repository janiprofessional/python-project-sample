word="programming"
character="g"
count=0
duplicate_chars = []
for i in word:
    if i in character:
        count += 1
print(count)

# output
# 2

word2 = "programming"
characters = ["g",'m']
count2=0
for duplicate in word2:
    if duplicate in characters:
        count2+=1

print(count2)

# output 
# 4