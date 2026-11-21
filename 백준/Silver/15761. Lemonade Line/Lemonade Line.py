for x in sorted(map(int,[*open(s:=0)][1].split()))[::-1]:s+=s<=x
print(s)