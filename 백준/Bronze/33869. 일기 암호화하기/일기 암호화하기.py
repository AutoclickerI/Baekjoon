v='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=''
for i in input()+v:s+=i[i in s:]
print(input().translate(v.maketrans(v,s)))