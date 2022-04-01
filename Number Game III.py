n, ans = input(), 0
for x in n:
    while n[int(x[-1]) - 1] not in x:
        x += n[int(x[-1]) - 1]
    ans = max(ans, int(x))
print(ans)
