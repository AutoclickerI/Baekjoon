l,r,u,d=[],[],[],[]
for i in[*open(0)][1:]:x,y,c=i.split();[u,l,r,d][ord(c)%5]+=int((y,x)[c in'LR']),
try:v=(min(l)+~max(r))*(min(d)+~max(u))
except:v='Infinity'
print(v)