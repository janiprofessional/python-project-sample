vowels = ['a', 'e', 'i', 'o', 'u']
word = 'programming'
count = 0
vowel_list = []
for character in word:
    if character in vowels:
        count += 1
        #print(character)
        vowel_list.append(character)

print(count)
vowel_list.sort()
print(vowel_list)

# output:
# 3
#['a', 'i', 'o']
