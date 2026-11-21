def f():s=input();return int(s[:2])*60+int(s[3:])
t=f()-f()
print(min(t%720,-t%720)*6)