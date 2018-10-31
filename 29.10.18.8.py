a = input('Enter the word: ')
def func(a):
    x = len(list(a))
    y = len(set(a))
    if x == y:
        return 'True'
    else:
        return 'False'

print(func(a))
