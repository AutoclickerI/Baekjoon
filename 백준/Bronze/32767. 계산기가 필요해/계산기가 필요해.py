c,*l=input().split()
for i,j in zip(*[iter(l)]*2):
    c=str(eval(c+i+j))
print('''=================
|SASA CALCULATOR|
|%15s|
-----------------
|               |
| AC         /  |
| 7  8  9    *  |
| 4  5  6    -  |
| 1  2  3    +  |
|    0  .    =  |
================='''%f'{eval(c):.3f}')