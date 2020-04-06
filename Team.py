count = 0
N = int(input(''))
for i in range(N):
    X, Y, Z = map(int, input('').split())
    sum = X + Y + Z
    if sum >= 2:
        count += 1
print(count)