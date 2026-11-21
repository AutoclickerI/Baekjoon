*s,=sorted(map(int,input()))
if 0 not in s or sum(s)%3:print(-1)
else:print(*s[::-1],sep='')