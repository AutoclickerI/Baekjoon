def solution(triangle):
    v=triangle[0]
    for i in triangle[1:]:
        s=[0]*len(i)
        for j in range(len(v)):
            s[j]=max(s[j],v[j]+i[j])
            s[j+1]=max(s[j+1],v[j]+i[j+1])
        v=s
    return max(v)