[i,*_],B,C,D=[sorted(map(int,i.split()))for i in open(0)]
print(y:=sum(B+C+D),y-sum(B[-i:]+C[-i:]+D[-i:])//10)