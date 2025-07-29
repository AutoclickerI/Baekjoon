a,b,c=[eval(i.replace(' ','*60+'))for i in open(0)]
print(sum(str(c)in f'{i+i//60*40:04}'for i in range(a,b+1)))