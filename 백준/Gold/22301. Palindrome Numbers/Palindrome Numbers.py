for _ in[0]*int(input()):
    l=len(s:=str(n:=int(input())))
    t=s[:l//2+l%2]
    if t[::-1]<s[l//2:]:t=str(int(t)+1) 
    print(t+t[l%-2-1::-1])