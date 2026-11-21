s=[]
f=s.index
I=input
exec("s+='{%s}'%','.join(s),;"*16+'print(s[f(I())+f(I())]),'*int(I()))