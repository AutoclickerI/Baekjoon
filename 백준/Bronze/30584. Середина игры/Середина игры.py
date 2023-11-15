p,q=map(int,open(0))
if p+q&1:print('Error')
elif p>1<q:print('Undefined')
else:print(p//2,q//2,p%2)