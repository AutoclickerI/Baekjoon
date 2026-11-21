string line = Stdio.stdin->gets();
int main(){
    int n;
    sscanf(line,"%d",n);
    write((n*860798509+198609463)%1000000007+"\n");
}