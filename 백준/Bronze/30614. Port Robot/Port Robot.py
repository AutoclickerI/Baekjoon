s=''
f=1
input()
for i in input():
  if i<'[':f&=s[-1:]==i.lower();s=s[:-f]
  else:s+=i
print((s<' ')*f)