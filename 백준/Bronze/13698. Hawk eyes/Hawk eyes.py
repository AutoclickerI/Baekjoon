l=[0,1,0,0,2]
for i in input():p,q=[1,1,1,2,2,3,2,3,4,3,4,4][ord(i)-65::6];l[p],l[q]=l[q],l[p]
print(*map(l.index,[1,2]))