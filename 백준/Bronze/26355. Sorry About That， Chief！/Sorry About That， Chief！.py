p=[0,0]+[1]*10006
for i in range(2,98):
    if p[i]:p[2*i::i]=[0]*(10007//i-1)
_,*a=map(int,open(0).read().split())
for i in a:
    print('Input value:',i)
    if p[i]:print('Would you believe it; it is a prime!\n')
    else:
        for j in range(1,99):
            if p[i-j]|p[i+j]:print(f'Missed it by that much ({j})!\n');break