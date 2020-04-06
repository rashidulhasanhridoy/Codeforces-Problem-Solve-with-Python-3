X = str(input(''))
Y = str(input(''))
if X.lower() == Y.lower():
    print('0')
elif X.lower() < Y.lower():
    print('-1')
elif X.lower() > Y.lower():
    print('1')