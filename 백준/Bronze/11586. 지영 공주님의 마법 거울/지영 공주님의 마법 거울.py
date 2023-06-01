l=[input()for i in[0]*int(input())]
p,q=[0,[1,1],[-1,1],[1,-1]][int(input())]
for i in l[::q]:print(i[::p])