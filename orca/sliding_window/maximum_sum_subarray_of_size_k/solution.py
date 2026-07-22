N,k=map(int,input().split())
a =list(map(int,input().split()))
m=sum(a[:k])
for i in range(len(a)-k+1):
    s=sum(a[i:i+k])
    m=s if s>m else m
print(m)
        

