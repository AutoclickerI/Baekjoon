p,q=[int(i[:2])*60+int(i[3:])for i in open(0)]
t=p-q
print(min(t%720,-t%720)*6)