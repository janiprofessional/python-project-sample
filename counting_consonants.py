vowels=['a','e','i','o','u']
word='programming'
count=0
consonant_list = []
for character in word:
    if character not in vowels:
        consonant_list.append(character)
        count+=1

print(count)
print(consonant_list)
# we can use sorted method for sorting and it it returns new list obj
sorted_list = sorted(consonant_list)
print(sorted_list)

#output: 
# 8
# ['p', 'r', 'g', 'r', 'm', 'm', 'n', 'g']
# ['g', 'g', 'm', 'm', 'n', 'p', 'r', 'r']
