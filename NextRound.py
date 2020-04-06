count = 0
n, k = map(int, input('').split())
X = list(map(int, input('').split()))
for i in X:
  if i > 0 and i >= X[k - 1]:
      count += 1
print(count)