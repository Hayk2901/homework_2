n = int(input())

m = n
s = 1
while m >= 3:
    s *= 3
    m //= 3
print(s)
