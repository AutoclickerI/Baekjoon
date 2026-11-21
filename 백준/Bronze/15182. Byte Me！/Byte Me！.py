_,*l=[i[::2]for i in open(0)]
k,K=[[i.count('1')&1for i in l]for l in[zip(*l),l]]
b=k.count(1)==1
s='B%s %d is broken'
print(b*'Even'or'Odd',s%('yte',K.index(b)+1),s%('it',k.index(b)+1))