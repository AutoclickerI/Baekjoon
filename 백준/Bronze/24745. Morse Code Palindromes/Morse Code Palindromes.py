d={"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".","F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---","K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---","P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-","U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--","Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--","4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..","9":"----."}
s=''
f=0
for i in list(input()):
    try:s+=d[i.upper()]
    except:0
for i in range(len(s)//2):
    if s[i]!=s[-1-i]:
        f=1
print('NO'if f!=0 else'NO'if s=='' else'YES')