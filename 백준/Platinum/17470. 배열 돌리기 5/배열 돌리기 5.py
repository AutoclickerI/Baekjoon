N,M,R=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]
*l,=map(int,input().split())

sub=[[1,2],[3,4]]
main=[[1,2],[3,4]]

for i in l:
    if i==1:
        main=main[::-1]
        sub=sub[::-1]
    if i==2:
        main=[i[::-1]for i in main]
        sub=[i[::-1]for i in sub]
    if i==3:
        main=[[*i][::-1]for i in zip(*main)]
        sub=[[*i][::-1]for i in zip(*sub)]
    if i==4:
        main=[[*i]for i in zip(*[i[::-1]for i in main])]
        sub=[[*i]for i in zip(*[i[::-1]for i in sub])]
    if i==5:
        main=[[*i][::-1]for i in zip(*main)]
    if i==6:
        main=[[*i]for i in zip(*[i[::-1]for i in main])]

subch=[[1,2],[3,4]]
mainch=[[1,2],[3,4]]

while sum(mainch[0])!=sum(main[0]):
    b=[[*i][::-1]for i in zip(*b)]
    mainch=[[*i][::-1]for i in zip(*mainch)]
    subch=[[*i][::-1]for i in zip(*subch)]

if mainch[0]!=main[0]:
    b=[i[::-1]for i in b]
    mainch=[i[::-1]for i in mainch]
    subch=[i[::-1]for i in subch]
N,M=len(b),len(b[0])
mat=[[i[:M//2]for i in b[:N//2]],[i[M//2:]for i in b[:N//2]],[i[:M//2]for i in b[N//2:]],[i[M//2:]for i in b[N//2:]]]

while sum(subch[0])!=sum(sub[0]):
    for i in range(4):
        mat[i]=[[*i][::-1]for i in zip(*mat[i])]
    subch=[[*i][::-1]for i in zip(*subch)]

if subch[0]!=sub[0]:
    for i in range(4):
        mat[i]=[i[::-1]for i in mat[i]]
p,q,r,s=mat
for i,j in[*zip(p,q),*zip(r,s)]:
    print(*i,*j)