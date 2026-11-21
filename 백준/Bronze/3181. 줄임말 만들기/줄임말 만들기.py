s,*l=input().split()
for i in s,*[i for i in l if i not in['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']]:print(end=i[0].upper())