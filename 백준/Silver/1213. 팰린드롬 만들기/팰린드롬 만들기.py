i=input()
a=e=''
for k in sorted({*i}):c=i.count(k);a+=c//2*k;e+=c%2*k
print(e[1:]and"I'm Sorry Hansoo"or a+e+a[::-1])