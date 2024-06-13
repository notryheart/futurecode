"""def to_tri(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n%3) + s
        n //= 3
    return s"""
for N in range(1,100):
    s = bin(N)[2:]
    suma = 0
    for i in range(len(s)):
        suma += int(s[i])
    s = s + str(suma%2)
    s = s + str(N%2)
    print(N,int(s,2))