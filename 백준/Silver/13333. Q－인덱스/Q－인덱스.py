for i in sorted(map(int,[*open(r:=0)][1].split()))[::-1]:r+=r<i
print(r)