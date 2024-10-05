s=[1,5,10,50,100,250,500,1000,5000,10000]
n,*a,t=map(int,open(0).read().split())
s=[100*s[i]for i in range(10)if-~i not in a]
print('no '*(t*len(s)<=sum(s))+'deal')