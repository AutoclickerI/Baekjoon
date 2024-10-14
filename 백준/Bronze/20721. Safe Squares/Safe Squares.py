r=[1]*8
c=r[:]
for i in range(8):
 for j,x in enumerate(input()):f='R'>x;r[i]&=f;c[j]&=f
print(sum(r)*sum(c))