l=[1]
for i in range(20):l+=l[-1]*-~i,
N,K=map(int,input().split())
p=lambda tot,n,li:(n<1)*li or[li.pop(n//l[tot-1])]+p(tot-1,n%l[tot-1],li)

o=lambda tot,li:+(li==[])or l[tot-1]*sorted(li).index(li[0])+o(tot-1,li[1:])

for _ in[0]*K:
    if'P'<input():
        print(o(N,[*map(int,input().split())]))
    else:
        print(*p(N,int(input())-1,[*range(1,N+1)]))