a=50
exec('x=10**(len(str(a:=a*2))+1>>1);print(a:=a//-x*-x);'*int(input()))