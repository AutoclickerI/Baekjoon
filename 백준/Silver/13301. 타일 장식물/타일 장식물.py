l=[[1,1]]
exec('p,q=l[-1];l+=[[p+q,p]];'*int(input()))
print(2*(p+q))