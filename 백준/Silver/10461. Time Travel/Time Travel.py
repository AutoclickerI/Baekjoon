v=43200
for i in open(0):a,b=map(int,i.split());r=int(v*(2*v-a)/abs(a-b)%v/60+.5);print(a,b,f'{r%720//60 or 12:02d}:{r%60:02d}')