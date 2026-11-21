n,a,b,s,t=map(int,open(0).read().split())
print([['Full','Outside'][s<=a>=t or s>=b<=t],'City'][a<s<b>t>a])