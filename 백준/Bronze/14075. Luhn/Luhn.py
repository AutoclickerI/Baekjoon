l=input()
s=0
for i in range(len(l)):
    p=int(l[i])*(2-(i%2))
    s+=p%10+p//10
print('DNAE'[s%10!=0::2])