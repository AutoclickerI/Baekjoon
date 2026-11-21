s,a,b=open(0).read().split()
print(len({t for j in range(len(s)+1)for i in range(j)if(t:=s[i:j])[:len(a)]==a and t[-len(b):]==b}))