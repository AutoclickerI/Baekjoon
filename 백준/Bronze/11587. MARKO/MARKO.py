_,*W,s=open(0)
print(sum(all(i in'abc def ghi jkl mno pqrs tuv wxyz'.split()[int(j)-2]for i,j in zip(w,s[:-1]))for w in W))