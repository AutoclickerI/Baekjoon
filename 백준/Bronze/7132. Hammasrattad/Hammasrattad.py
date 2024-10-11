R=range(*eval(input().replace(' ',',1+')))
print(len({i/j for i in R for j in R}))