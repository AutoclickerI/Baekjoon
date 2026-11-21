l=sorted(open(0))
R=i=0
while i<8:R+=[10,8,6,5,4,3,2,1][i]*((l[i][9]>'B')*2-1);i+=1
print('BRleude'[R>0::2])