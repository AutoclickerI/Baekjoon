s=len(l:=input().split())
print(*[['EI'],['JAH']+l[:s//2]+l[~-s//2::-1]][sum(l[i]>l[~i]for i in range(s))<2])