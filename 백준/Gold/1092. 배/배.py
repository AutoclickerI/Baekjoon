_,c,[p],l=eval('sorted(map(int,input().split())),'*4)
print(-(c[-1]<l[-1])or-~max(m//sum(a>=l[~m]for a in c)for m in range(p)))