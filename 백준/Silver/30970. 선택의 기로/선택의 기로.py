l1=[]
l2=[]
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    l1+=(-p,q),
    l2+=(q,-p),
l1.sort()
l2.sort()
print(-l1[0][0],l1[0][1],-l1[1][0],l1[1][1])
print(-l2[0][1],l2[0][0],-l2[1][1],l2[1][0])