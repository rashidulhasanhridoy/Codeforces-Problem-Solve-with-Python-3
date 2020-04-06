sum = 0
N = int(input(''))
for i in range(N):
    X = str(input(''))
    if X == 'X++':
        sum = sum + 1
    elif X == 'X--':
        sum = sum - 1
    elif X == '--X':
        sum = sum - 1
    elif X == '++X':
        sum = sum + 1
print(sum)