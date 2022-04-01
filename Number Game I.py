n = int(input())
while n != 1:
    print(n)
    n = 3 * n + 1 if n % 2 else n // 2
print(1)