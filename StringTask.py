X = str(input(''))
Y = X.lower()
for i in Y:
    if i != 'a' and i != 'e' and i != 'o' and i != 'i' and i != 'u'and i != 'y':
        print('.', i, sep = '', end = '')