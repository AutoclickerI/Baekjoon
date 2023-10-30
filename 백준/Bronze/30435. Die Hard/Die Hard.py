l=[[*map(int,input().split())]for _ in[0]*3]
for i in range(3):
    flag=1
    for j in{0,1,2}-{i}:
        if sum((p>q)-(p<q)for p in l[i]for q in l[j])<0 or all(p==q for p in l[i]for q in l[j]):
            flag=0
    if flag:
        exit(print(i+1))
print('No dice')