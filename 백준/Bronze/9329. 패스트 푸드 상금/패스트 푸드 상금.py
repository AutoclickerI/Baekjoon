l=[[*map(int,i.split())]for i in open(0)]
n=0
while l:=l[n+1:]:[n,_],*l=l;print(sum(v*min(l[n][j-1]for j in z)for _,*z,v in l[:n]))