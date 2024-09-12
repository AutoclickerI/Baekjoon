for i in sorted(map(int,[*open(a:=0)][1].split()))[::-1]:
 if i<a:break
 a+=1
print(a)