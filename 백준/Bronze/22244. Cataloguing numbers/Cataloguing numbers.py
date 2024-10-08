from datetime import date
for _ in'   ':
    s=input()
    try:d,m,y=map(int,[s[:2],s[2:4],s[4:7]]);date(y+1000*(1+(y<600)),m,d);print((s[7]in'169')*(int(s[8])==sum(int(s[i])**2for i in range(8))%7))
    except:print(0)