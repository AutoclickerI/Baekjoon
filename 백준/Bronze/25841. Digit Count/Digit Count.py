p,q,r=input().split()
print(sum(str(i).count(r)for i in range(int(p),int(q)+1)))