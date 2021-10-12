n = int(input())

def summ(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

while n >= 10:
    n = summ(n)
    print(n)
