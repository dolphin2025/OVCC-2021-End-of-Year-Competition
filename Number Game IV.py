B = int(input()) - 1
N = [int(i) - 1 for i in input().split()]
l = {}
cycle = set()

for i in range(B):
    if i not in l:
        num = [i]
        seen = {i}
        while N[num[-1]] not in seen and N[num[-1]] not in l:
            seen.add(N[num[-1]])
            num.append(N[num[-1]])
        if N[num[-1]] in l:
            run = l[N[num[-1]]]
            run -= N[num[-1]] in cycle
            for i in num[::-1]:
                run += 1
                l[i] = run
        else:
            cstart = num.index(N[num[-1]])
            clen = len(num) - cstart
            for i in num[cstart:]: l[i] = clen
            for i in num[:cstart][::-1]:
                cycle.add(i)
                l[i] = clen
                clen += 1
m = max([l[i] for i in l])
mlen = [i for i in l if l[i] == m]
mnum = max(mlen, key=lambda x: N[x])
ans = [N[mnum]]
seen = set(ans)
while N[ans[-1]] not in seen:
    seen.add(N[ans[-1]])
    ans.append(N[ans[-1]])
print(' '.join([str(i + 1) for i in ans]))
