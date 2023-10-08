s=input()
S='kick'
idx=0
cnt=0
for i in s:
    if i==S[idx]:
        idx+=1
    else:
        idx=i=='k'
    if idx==4:
        idx=1
        cnt+=1
print(cnt)