class resistance:
    def __init__(self,R):
        self.R=R
    def __or__(self,R):
        return resistance(1/(1/R.R+1/self.R))
    def __sub__(self,R):
        return resistance(R.R+self.R)
input()
for i,j in enumerate(input().split(),1):
    exec(f'R{i}=resistance({j})')
print(eval(input()).R)