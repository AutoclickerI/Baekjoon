a=0
for s in[*open(0)][1].split():
 c=[0]*3    
 for i,t in enumerate(s):f=t in'aeiouy';c[2]+=1-f;c[i%2^f]+=1
 a+=min(c)
print(a)