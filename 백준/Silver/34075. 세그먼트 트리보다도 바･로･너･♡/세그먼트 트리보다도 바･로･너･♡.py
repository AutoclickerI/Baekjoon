N=int(input())
l=[input().split()for _ in[0]*N]

M=int(input())
d=[input().split()for _ in[0]*M]
d={i:int(j)for i,j in d}

for _ in[0]*int(input()):
    s=input()
    if s[-1]=='!':
        v=d[s.split()[0]]
        print('hai!')
    else:
        l.sort(key=lambda i:(abs(int(i[1])-v),i[0]))
        print(l[1][0],'yori mo',l[0][0])