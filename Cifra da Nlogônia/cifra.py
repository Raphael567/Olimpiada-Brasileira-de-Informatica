alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

word = "ter"
cipher = ""

for letter in word:
    if letter in vowels:
        cipher += letter
    else:
        index = alp.index(letter)

        for v_index in [alp.index(v) for v in vowels]:
            if v_index > index:
                closest_vowel_index = v_index

        for c_index in [alp.index(c) for c in alp]:
            if letter != 'z':
                if c_index > index and not alp[c_index] in vowels:
                    next_consonant_index = c_index
                    break
            else:
                next_consonant_index = c_index

        cipher += alp[index] + alp[closest_vowel_index] + alp[next_consonant_index]
print(cipher)

# cipher = ""
# temp = ""
#
# for i in range(len(word_letters)):
#     print(temp)
#     if word_letters[i] == alp[original_consonants[i]]:
#         temp += alp[original_consonants[i]]
#         for i2 in range(len(vowels)):
#             if alp[original_consonants[i]+1] == vowels[i2]:
#                 temp += vowels[i2]
#                 if alp[original_consonants[i] +1] == vowels[i2]:
#                     temp += alp[original_consonants[i]+2]
#                 else:
#                     temp += alp[original_consonants[i]+1]
#         cont = 0
#         temp += alp[original_vowels[cont]]
#         cont += 1
#
# print(temp)


# for letter in word:
#     if letter in vowels:
#         cipher += letter
#     else:
#         index = alp.index(letter)
#
#         closest_vowel_index = index
#
#         for v_index in [alp.index(v) for v in vowels]:
#             if v_index >= index:
#                 closest_vowel_index = v_index
#                 break
#
#         for c_index in [alp.index(c) for c in alp]:
#             if c_index > index:
#                 next_consonant_index = c_index
#                 break
#
#         cipher += alp[index] + alp[closest_vowel_index] + alp[next_consonant_index]
#
# print(cipher)
