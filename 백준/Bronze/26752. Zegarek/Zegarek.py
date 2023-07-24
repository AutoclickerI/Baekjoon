p,q,r=map(int,input().split())
t=p*3600+q*60+r+1
print(f'{t//3600%24:02d}:{t//60%60:02d}:{t%60:02d}')