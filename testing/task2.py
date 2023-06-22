

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']

dictionary = {}
for index, letter in enumerate(alphabet):
    dynamic_index = index
    if letter in vowels:
        while True:
            dynamic_index -= 1
            if alphabet[dynamic_index] in consonants:
                dictionary[letter] = alphabet[dynamic_index]
                break
    else:
        while True:
            dynamic_index += 1
            if dynamic_index == len(alphabet):
                dynamic_index = 0
            if alphabet[dynamic_index] in vowels:
                dictionary[letter] = alphabet[dynamic_index]
                break


def replace_with_dictionary(dictionary, word):
    result = []
    for char in word:
        result.append(dictionary[char])
    return ''.join(result)


def replace_characters(word):
    result = []

    for char in word:
        if char in vowels:
            vowel_index = alphabet.index(char)
            left_consonant = consonants[(vowel_index - 1) % len(consonants)]
            result.append(left_consonant)
        elif char in consonants:
            consonant_index = alphabet.index(char)
            right_vowel = vowels[(consonant_index + 1) % len(vowels)]
            result.append(right_vowel)

    return ''.join(result)


input1 = 'cat'
output1 = replace_with_dictionary(dictionary, input1)
print(output1)

input2 = 'abcdtuvwxyz'
output2 = replace_with_dictionary(dictionary, input2)
print(output2)