n=int(input())
l=[input().replace(*'.0').replace(*'#1')for _ in[0]*5]
num=[tuple(int(j[4*i:4*i+3],2)for j in l)for i in range(n)]
d={0: (7, 5, 5, 5, 7),
 1: (1, 1, 1, 1, 1),
 2: (7, 1, 7, 4, 7),
 3: (7, 1, 7, 1, 7),
 4: (5, 5, 7, 1, 1),
 5: (7, 4, 7, 1, 7),
 6: (7, 4, 7, 5, 7),
 7: (7, 1, 1, 1, 1),
 8: (7, 5, 7, 5, 7),
 9: (7, 5, 7, 1, 7)}
try:
    val=0
    for i in num:
        check=[all(i[k]|d[j][k]==d[j][k]for k in range(5))for j in range(10)]
        assert any(check)
        cnt=sum(check)
        val*=10
        val+=sum(i*check[i]for i in range(10))/cnt
    print(val)
except:
    print(-1)