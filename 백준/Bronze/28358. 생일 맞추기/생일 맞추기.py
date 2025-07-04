l=[31,29,31,30,31,30,31,31,30,31,30,31]
for v in[*open(0)][1:]:
 a=0;s={str(i)for i in range(10)if'0'<v[i*2]}
 for i in range(12):
  for j in range(l[i]):
   a+=s-{*f'{i+1}{j+1}'}==s
 print(a)