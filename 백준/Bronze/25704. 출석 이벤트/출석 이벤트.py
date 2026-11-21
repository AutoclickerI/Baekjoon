p,q=map(int,open(0))
print(max(0,q-max([0,500,q//10,2000,q//4][:p//5+1])))