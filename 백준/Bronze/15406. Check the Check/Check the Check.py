*l,n=map(eval,[i.replace(*' *')for i in[*open(0)][1::2]])
print(['PAY','PROTEST'][sum(l)<n])