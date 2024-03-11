input()
*l,=map(int,input().split())
p=l[0]
print(max(j-(p:=p if i<j else j)for i,j in zip(l,l[1:])))