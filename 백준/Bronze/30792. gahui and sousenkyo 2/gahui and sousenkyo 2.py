_,(n,),l=[map(int,i.split())for i in open(0)]
print(sum(n<i for i in l)+1)