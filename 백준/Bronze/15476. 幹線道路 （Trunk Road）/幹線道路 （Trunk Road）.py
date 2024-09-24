H,W=map(int,input().split())
a=eval('[*map(int,input().split())],'*H)
print(min(min(sum(sum(a[s][t]*min(abs(i-s),abs(j-t))for t in range(W))for s in range(H))for j in range(W))for i in range(H)))