l=[1]
for i in range(20):l+=l[-1]*-~i,
N,K=map(int,input().split())
def get_perm(tot,n,li):
    if n<1:
        return li
    return [li.pop(n//l[tot-1])]+get_perm(tot-1,n%l[tot-1],li)

def get_order(tot,li):
    if li==[]:
        return 1
    return l[tot-1]*sorted(li).index(li[0])+get_order(tot-1,li[1:])

for _ in[0]*K:
    if'P'<input():
        print(get_order(N,[*map(int,input().split())]))
    else:
        print(*get_perm(N,int(input())-1,[*range(1,N+1)]))