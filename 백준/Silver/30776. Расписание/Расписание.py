from calendar import*
from datetime import*

def count(y):
    w=[0]*7
    for m in range(12):
        for d in range(monthrange(y,m+1)[1]):w[weekday(y,m+1,d+1)]+=1
    return w

N=int(input())
y=int(input())
day=count(y)
holy=[0]*7
for _ in[0]*N:
    d,m=input().split()
    holy[weekday(y,datetime.strptime(m,'%B').month,int(d))]+=1
l=[(day[i]+sum(holy[j]for j in range(7)if i!=j),i)for i in range(7)]
print(day_name[max(l)[1]],day_name[min(l)[1]])