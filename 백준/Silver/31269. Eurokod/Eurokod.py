N=n=int(input())
*l,=map(int,input().split())
a=[0]*n
for i in l:
    a[i-1]=N
    N-=1
*s,=map(int,input().split())
d={j:i for i,j in enumerate(sorted(s))}
d={i:d[i]for i in s}
k=0
for i in sorted(range(n),key=lambda i:(-a[i]-d[s[i]],-d[s[i]])):
    k+=1
    print(f'{k}. Kod{i+1:02d} ({1+d[s[i]]+a[i]})')