W = []
S = str(input(''))
for i in S:
    if i not in W:
        W.append(i)
if len(W) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')