r=[1,1,1]
exec('r+=r[-1]+r[-3],;'*int(input()))
print(r[-4])