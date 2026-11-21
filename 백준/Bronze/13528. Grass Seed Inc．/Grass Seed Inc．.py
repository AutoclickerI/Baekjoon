I=input
print(eval(I())*sum(eval(I().replace(' ','*'))for _ in[0]*int(I())))