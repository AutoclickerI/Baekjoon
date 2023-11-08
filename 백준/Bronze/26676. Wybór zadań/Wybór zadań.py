d={f'{i+1}{c}':-~(i>3)for i in range(5)for c in'ABC'}
input()
for i in input().split():
    d[i]-=1
print('NTIAEK'[max(d.values())<1::2])