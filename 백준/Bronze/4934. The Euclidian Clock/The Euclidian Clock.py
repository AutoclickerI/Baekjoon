f=lambda:[*map(eval,input().split())]
g=lambda h,m,s,u:h*30+m/2+s/120+u/12000
import math
for T in range(*f()):print(f'{T+1}. {(g(*f())-g(*f()))/360*math.pi*f()[0]**2:.3f}')