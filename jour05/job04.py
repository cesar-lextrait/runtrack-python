def cesar(z, message):

    crypte= ''
    for i in range(len(message)):
        char = message[i]
        crypte += chr((ord(char) + z - 96 ) % 26 + 96)
    print(crypte)
cesar(4, 'abcd ')
cesar(3, 'laviecpasfacile')