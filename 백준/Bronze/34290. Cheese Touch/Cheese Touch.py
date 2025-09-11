p,t,*m=map(int,input().split())
for i in input().split('W'):t-=({*i}=={'H'})*1e9;s,*l,e=[*map(len,i.split('I'))]*2;m+=s,e,*[j+1>>1for j in l]
print(['CURED','ALL INFECTED'][max(m)*p<t])