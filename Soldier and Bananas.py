sum = 0
k, n, w = map(int, input('').split())
for i in range(1, w + 1):
    sum += k * i
if sum > n:
    print('%d' %(sum - n))
else:
    print('0')