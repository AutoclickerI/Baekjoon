N=int(input())
M=int(input())
*l,=range(N)

def f(n):
    if n!=l[n]:
        l[n]=f(l[n])
    return l[n]

for s in range(N):
    v=input()
    for e in range(N):
        if'0'<v[2*e]:
            p,q=sorted((f(s),f(e)))
            l[q]=p

if len({f(int(i)-1)for i in input().split()})==1:
    print('YES')
else:
    print('NO')