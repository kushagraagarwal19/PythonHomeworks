import string

def printString(character, number):
    character = character.lower()
    a = list(string.ascii_lowercase)
    index = a.index(character)
    stringFinal = ''
    for i in range(number):
        if(index > 25):
            index = 0
        stringFinal = stringFinal + a[index]
        index = index + 1
    print(stringFinal)

printString('A', 45)