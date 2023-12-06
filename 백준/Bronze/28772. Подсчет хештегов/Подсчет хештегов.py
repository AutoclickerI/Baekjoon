s=input().split()
print(len(l:={i for i in s if'#'==i[0]and 1<len(i)and i.count('#')==1}))
for i in sorted(l):print(i,s.count(i))