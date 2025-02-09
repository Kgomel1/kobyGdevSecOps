# ex3
NUMBER_OF_TIMES = 3
found: bool = False
array = []
hash = {}
while not found:
    word = input('please enter word:')
    for value in array:
        if value == word:
            if word in hash.keys():
                hash[word]+=1
            else:
                hash[word] = 1
            if hash[word] == NUMBER_OF_TIMES:
                found = True
    array.append(word)

print(f'{word} found {NUMBER_OF_TIMES}')