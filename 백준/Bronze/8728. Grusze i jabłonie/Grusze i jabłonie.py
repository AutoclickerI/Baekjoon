_,l=open(0)
print(max(map(lambda x,y:abs(l.find(x)-l.rfind(y))//2,'01','10')))