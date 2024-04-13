for i in sorted(map(int,[*open(0)][a:=1].split())):a+=i*(i<=a)
print(a)