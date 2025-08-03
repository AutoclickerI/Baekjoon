r=[0]*26
for s in[*open(0)][1:]:
 for i in range(26):r[i]+=max(map(str.count,s.split(),[chr(i+97)]*2))
print(*r)