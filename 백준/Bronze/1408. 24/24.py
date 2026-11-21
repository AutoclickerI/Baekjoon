a,b,c,d,e,f=map(int,open(0).read().replace(*': ').split())
n=((d-a)*3600+(e-b)*60+f-c)%86400
print(f'{n//3600:02d}:{n%3600//60:02d}:{n%60:02d}')