n = int(input())
for i in range(n + 1, n + 9):
    if i % 2 and not all(i % d for d in range(2, int(i**.5)+1)):
        print(i)
        break