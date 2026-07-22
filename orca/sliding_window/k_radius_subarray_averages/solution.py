a=list(map(int,input().split()))
k =int(input())
res=[-1]*len(a)
for i in range(k,len(a)-k):
    res[i] = sum(a[i - k : i + k + 1]) // (2 * k + 1)

print(*res)

