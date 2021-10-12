n = int(input())
i = 1
k = 0
while i <= n:
    if n % i == 0:
        k += 1
    i += 1
print(k)
