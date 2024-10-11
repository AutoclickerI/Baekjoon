s=[(i:=0,1e9)]
for a in map(int,[*open(0)][1].split()):
 while s[-1][1]<a:s.pop()
 print(s[-1][0]);s+=(i:=i+1,a),