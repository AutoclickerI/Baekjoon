n=int(input())
R=range(10)
try:[print(f'{p:7}\n+{q:6}\n-------\n{n:7}')*1for d in R for r in R for w in R[1:]for o in R for l in R for e in R for h in R[1:]if(p:=10000*h+1000*e+110*l+o)==n-(q:=10000*w+1000*o+100*r+10*l+d)and len({h,e,l,o,w,r,d})==7]
except:0
else:print('No Answer')