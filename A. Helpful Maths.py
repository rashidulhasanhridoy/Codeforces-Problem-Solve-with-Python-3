Numbers = []
count = 0
N = str(input(''))
for i in N:
    if i != '+':
        Numbers.append(i)
    else:
        count += 1
Numbers = sorted(Numbers)
for j in Numbers:
    print(j, end = '')
    if count != 0:
        print('+', end = '')
        count -= 1