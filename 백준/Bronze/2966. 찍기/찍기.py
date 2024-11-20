_,s=open(0)
a,b,c=[sum(i==j for i,j in zip(s,x*99))for x in['ABC','BABC','CCAABB']]
print(m:=max(a,b,c),'Adrian '*(m==a)+'Bruno '*(m==b)+'Goran'*(m==c))