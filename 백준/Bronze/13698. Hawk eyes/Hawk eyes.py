l=[0,1,0,0,2]
for i in input():p,q=[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]][ord(i)-65];l[p],l[q]=l[q],l[p]
print(*map(l.index,[1,2]))