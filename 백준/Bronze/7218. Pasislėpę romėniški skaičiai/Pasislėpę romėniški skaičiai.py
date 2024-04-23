_,S=open(0)
print(*[i+1for i in range(12)if'I II III IV V VI VII VIII IX X XI XII'.split()[i]in S])