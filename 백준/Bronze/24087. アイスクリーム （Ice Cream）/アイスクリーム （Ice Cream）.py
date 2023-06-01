S,A,B=[int(input())for _ in[0]*3]
if S>A:print(250+(S-A)//B*100+100*min((S-A)%B,1))
else:print(250)