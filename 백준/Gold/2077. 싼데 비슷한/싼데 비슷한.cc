#include <iostream>

using namespace std;

int c[4], N, T, tmp, min_idx, min_val;

int main(){
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
    cin >> T;
    while (T--){
        cout<<"YES\n";
        cin >> N;
        c[0]=c[1]=c[2]=c[3]=0;
        for (int i=0;i<N;i++){
            cin >> tmp;
            c[i%4] += tmp;
        }
        min_val=2147483647;
        for (int i=0;i<(4<N?4:N);i++){
            if(c[i]<min_val){
                min_val=c[i];
                min_idx=i;
            }
        }
        if(min_idx){
            cout<<0;
            for(int i=1;i<min_idx;i++)
                cout<<min_idx-1;
            N-=min_idx;
        }
        while(4<N){
            cout<<"0333";
            N-=4;
        }
        cout<<0;
        for(int i=1;i<N;i++){
            cout<<N-1;
        }
        cout<<"\n";
    }
}