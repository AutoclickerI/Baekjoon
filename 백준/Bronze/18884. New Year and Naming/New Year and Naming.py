i,s,t,_,*l=open(0)
N,M=map(int,i.split())
s,t=s.split(),t.split()
for i in l:i=int(i)-1;print(s[i%N]+t[i%M])