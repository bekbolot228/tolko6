def word_w():
    a = input('Enter the santence: ')
    soz = a.split()
    return ''.join(tt[:1].capitalize() for tt in soz)
print(word_w())
