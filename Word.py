U = []
L = []
S = str(input(''))
for i in S:
    if ord(i) >= 65 and ord(i) <= 90:
        U.append(i)
    elif ord(i) >= 97 and ord(i) <= 122:
        L.append(i)
if len(U) > len(L):
    print(S.upper())
elif len(U) < len(L):
    print(S.lower())
elif len(U) == len(L):
    print(S.lower())