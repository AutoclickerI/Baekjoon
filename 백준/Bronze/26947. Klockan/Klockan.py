t=int(input())
while t%55:t+=3600
print('%02d:%02d'%divmod(t//55,60))