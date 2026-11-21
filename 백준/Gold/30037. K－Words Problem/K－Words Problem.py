for _ in[0]*int(input()):
    sentence=input().split()
    ptr=0
    while ptr<len(sentence):
        if sentence[ptr]=='of':
            if 0<=ptr-1 and ptr+1<len(sentence)and sentence[ptr+1]in['Korea','Korea.','Korea,','Korea!','Korea?']and sentence[ptr-1][-1]not in'.,?!':
                sentence[ptr-1]='K-'+sentence[ptr-1][0].upper()+sentence[ptr-1][1:]+sentence[ptr+1][5:]
                sentence.pop(ptr);sentence.pop(ptr)
                ptr-=1
        ptr+=1
    sentence=sentence[::-1]
    ptr=0
    while ptr<len(sentence):
        if sentence[ptr]=='Korea' and 0<=ptr-1:
            sentence[ptr-1]='K-'+sentence[ptr-1][0].upper()+sentence[ptr-1][1:]
            sentence.pop(ptr)
            ptr-=1
        ptr+=1
    print(' '.join(sentence[::-1]))