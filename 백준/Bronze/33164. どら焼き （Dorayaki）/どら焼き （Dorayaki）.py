_,A,B=eval('[*map(int,input().split())],'*3)
print(sum(max(a,b)*(a+b)for a in A for b in B))