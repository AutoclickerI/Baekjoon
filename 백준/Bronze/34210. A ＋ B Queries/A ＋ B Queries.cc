#include<vector>
using T=std::vector<int>;
T a,b;
void initialize(T A,T B){a=A;b=B;}int answer_question(int i,int j){return a[i]+b[j];}