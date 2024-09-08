for i in sorted(map(int,[*open(a:=0)][m:=1].split()))[::-1]:m/=2;a+=i*m
print(a)