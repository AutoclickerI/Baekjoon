I=input
d={}
for _ in[0]*int(I()):p,q=I().split();d[q]=p
for i in range(0,len(s:=I()),4):print(end=d.get(s[i:i+4],'?'))