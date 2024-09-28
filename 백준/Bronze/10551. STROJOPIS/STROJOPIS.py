d={}
for i in input():d[i]=d.get(i,0)+1
s="1QAZ2WSX3EDC4RFV5TGB6YHN7UJM8IK,9OL.0P;/-['=]"
t=[0,4,8,12,20,28,32,36,45]
for x,y in zip(t,t[1:]):print(sum(map(d.get,s[x:y],[0]*y)))