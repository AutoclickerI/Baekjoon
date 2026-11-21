f=0
for i in range(len(s:=''.join(input().lower().split()))):f|=len(t:=s[i:i+3])>len({*t})
print(['Anti-p','P'][f]+'alindrome')