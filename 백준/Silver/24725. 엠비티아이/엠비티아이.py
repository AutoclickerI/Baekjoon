a,b=list(map(int,input().split()))
c=[list(input())for i in range(a)]
num=0
for i in range(a):
    for j in range(b):
        try:
            if c[i][j]in['I','E']and c[i+1][j]in['N','S']and c[i+2][j]in['F','T']and c[i+3][j]in['P','J']:
                num+=1
            if c[i+3][j]in['I','E']and c[i+2][j]in['N','S']and c[i+1][j]in['F','T']and c[i][j]in['P','J']:
                num+=1
        except:0
        try:
            if c[i][j]in['I','E']and c[i][j+1]in['N','S']and c[i][j+2]in['F','T']and c[i][j+3]in['P','J']:
                num+=1
            if c[i][j+3]in['I','E']and c[i][j+2]in['N','S']and c[i][j+1]in['F','T']and c[i][j]in['P','J']:
                num+=1
        except:0
        try:
            if c[i][j]in['I','E']and c[i+1][j+1]in['N','S']and c[i+2][j+2]in['F','T']and c[i+3][j+3]in['P','J']:
                num+=1
            if c[i+3][j+3]in['I','E']and c[i+2][j+2]in['N','S']and c[i+1][j+1]in['F','T']and c[i][j]in['P','J']:
                num+=1
        except:0
        try:
            if c[i+3][j]in['I','E']and c[i+2][j+1]in['N','S']and c[i+1][j+2]in['F','T']and c[i][j+3]in['P','J']:
                num+=1
            if c[i][j+3]in['I','E']and c[i+1][j+2]in['N','S']and c[i+2][j+1]in['F','T']and c[i+3][j]in['P','J']:
                num+=1
        except:0
print(num)