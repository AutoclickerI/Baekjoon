*l,n=map(eval,open(0).read().replace(*' *').split()[1::2])
print(['PAY','PROTEST'][sum(l)<n])