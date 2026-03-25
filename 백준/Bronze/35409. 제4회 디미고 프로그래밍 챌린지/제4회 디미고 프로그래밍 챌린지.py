s='''06:30-09:00
09:50-10:00
10:50-11:00
11:50-12:00
12:50-13:50
14:40-14:50
15:40-15:50
16:40-22:50'''.split()
l=[i.split('-')for i in s]

h,m=map(int,input().split())
s=f'{h:02}:{m:02}'
print('NYoe s'[any(i<=s<=j for i,j in l)::2])