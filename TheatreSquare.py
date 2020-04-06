n, m, a = map(int, input('').split())
x = (m + a - 1) // a
y = (n + a - 1) // a
print('%d' %(x * y))