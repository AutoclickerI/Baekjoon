s=sum((ord(a)-38)%58for a in input())
print('It is'+' not'*any(s%i<1for i in range(2,s)),'a prime word.')