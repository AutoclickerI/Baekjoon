h,m=map(int,open(0))
*l,=map(lambda t:max(h*t**3-6*t**4+2*t*t+t,0),range(1,m+1))
print('The balloon does not touch ground in the given time.'*(0 not in l)or f'The balloon first touches ground at hour: {l.index(0)+1}')