p=int(input())
g=int(input())
r=int(input())
o=int(input())
t=int(input())
m=10**18
cnt=0
for i in range(1-t//-p):
    for j in range(1-t//-g):
        for k in range(1-t//-r):
            for l in range(1-t//-o):
                if i*p+j*g+k*r+l*o==t:
                    cnt+=1
                    print(f'# of PINK is {i} # of GREEN is {j} # of RED is {k} # of ORANGE is {l}')
                    m=min(m,i+j+k+l)
print(f'Total combinations is {cnt}.')
print(f'Minimum number of tickets to print is {m}.')