v=43200
for i in open(0):a,b=map(int,i.split());r=int(v*(2*v-a)/abs(a-b)/60+.5);print(a,b,f'{r%720//60or 12:02d}:{r%60:02d}')