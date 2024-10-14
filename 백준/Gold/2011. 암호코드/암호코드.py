dp=[(1,0)]
s=input().replace('10','a').replace('20','b')
f='0'in s
for i in range(len(s)):
    if s[i-1:i+1]in[*map(str,range(11,20)),*map(str,range(21,27))]:
        dp+=(sum(dp[-1]),sum(dp[-2])),
    else:
        dp+=(sum(dp[-1]),0),
if f:
    print(0)
else:
    print(sum(dp[-1])%1000000)