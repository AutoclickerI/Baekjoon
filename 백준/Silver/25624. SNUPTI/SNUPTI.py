p,q=map(int,input().split())
l=[input()for _ in[0]*q]
ll=[sorted(set([l[i][j]for i in range(q)]))for j in range(p)]
ss=1
aa=[]
for i in ll:
    ss*=len(i)
    aa+=i
if len(l)-len(set(l))or len(l)-ss or len(aa)-len(set(aa)):
    print("NO")
else:
    print("YES")
    for i in ll:print(''.join(i))