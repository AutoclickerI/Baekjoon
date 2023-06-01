a,b,c=map(int,input().split())
AF,BD=map(int,input().split())
CeEa=(a-BD)*(c-AF)/BD/AF
print(b/(1+CeEa)*CeEa)