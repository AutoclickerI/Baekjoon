#include <bits/stdc++.h>
using namespace std;

// Python 의 move(n, cube) 함수에 대응
string moveCube(int n, const string &cube) {
    string b = cube;
    char n1, n2, n3;
    if (n == 0) {
        n1 = b[1];  n2 = b[3];  n3 = b[12];
        b[1] = b[22]; b[3] = b[20]; b[20] = b[19]; b[22] = b[17];
        b[17] = b[5]; b[19] = b[7];  b[5]  = n1;     b[7]  = n2;
        b[12] = b[13]; b[13] = b[15]; b[15] = b[14]; b[14] = n3;
    }
    else if (n == 1) {
        n1 = b[4];  n2 = b[5];  n3 = b[0];
        b[4] = b[8];  b[5] = b[9];  b[8]  = b[20]; b[9]  = b[21];
        b[20] = b[12]; b[21] = b[13]; b[12] = n1;     b[13] = n2;
        b[0] = b[1];  b[1] = b[3];  b[3]  = b[2];  b[2]  = n3;
    }
    else {
        // n == 2
        n2 = b[2];  n1 = b[3];  n3 = b[4];
        b[2]  = b[12]; b[3]  = b[14]; b[14] = b[16]; b[12] = b[17];
        b[16] = b[9];  b[17] = b[11]; b[9]  = n1;     b[11] = n2;
        b[4]  = b[5];  b[5]  = b[7];  b[7]  = b[6];  b[6]  = n3;
    }
    return b;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    string line;
    getline(cin, line); // 잔여 newline 제거

    while(T--){
        // 빈 줄 건너뛰고 입력 받기
        string x1, x2, x3, x4;
        do { getline(cin, x1); } while(x1.empty());
        getline(cin, x2);

        vector<string> mid(2);
        for(int i = 0; i < 2; i++){
            getline(cin, mid[i]);
            // 공백 제거
            mid[i].erase(remove(mid[i].begin(), mid[i].end(), ' '), mid[i].end());
        }

        getline(cin, x3);
        getline(cin, x4);

        // Python 코드와 동일한 순서로 b 벡터 구성
        vector<string> b(6);
        b[0] = string() + x2[0] + x1[0];
        b[1] = string() + x2[1] + x1[1];
        b[2] = mid[0];
        b[3] = mid[1];
        b[4] = string() + x3[1] + x4[1];
        b[5] = string() + x3[0] + x4[0];

        // 넷에서 6개 face 추출
        vector<pair<int,int>> coords = {
            {0,0},{2,2},{2,0},{2,4},{4,0},{2,6}
        };
        string cube;
        cube.reserve(24);
        for(auto &p : coords){
            int y = p.first, x = p.second;
            cube += b[y].substr(x,2);
            cube += b[y+1].substr(x,2);
        }

        // 목표 상태(cube_end) 초기화
        string cube_end = cube;
        cube_end[16] = cube_end[17] = cube_end[19] = cube_end[18];
        cube_end[20] = cube_end[21] = cube_end[22] = cube_end[23];
        cube_end[8]  = cube_end[9]  = cube_end[11] = cube_end[10];

        // Python 의 corner/orientation 로직
        vector<array<int,3>> corners = {
            {2,9,4},{3,5,12},{1,13,20},{0,8,21},
            {6,11,16},{7,17,14},{19,15,22}
        };
        vector<array<int,3>> perms = {
            {0,1,2},{0,2,1},{1,0,2},
            {1,2,0},{2,1,0},{2,0,1}
        };

        for(int i = 0; i < 7; i++){
            for(int j = 0; j < 6; j++){
                char p = cube[corners[i][perms[j][0]]];
                char q = cube[corners[i][perms[j][1]]];
                char r = cube[corners[i][perms[j][2]]];
                if(p==cube[18] && q==cube[23])
                    cube_end[12]=cube_end[13]=cube_end[14]=cube_end[15]=r;
                if(p==cube[10] && q==cube[23])
                    cube_end[0]=cube_end[1]=cube_end[2]=cube_end[3]=r;
                if(p==cube[10] && q==cube[18])
                    cube_end[4]=cube_end[5]=cube_end[6]=cube_end[7]=r;
            }
        }

        // 양방향 BFS 준비
        unordered_map<string,int> distA, distB;
        distA.reserve(200000);
        distB.reserve(200000);
        queue<string> qa, qb;

        distA[cube] = 0;
        qa.push(cube);
        distB[cube_end] = 0;
        qb.push(cube_end);

        int answer = -1;
        bool done = false;
        while(!done){
            // 한 단계씩 A 쪽 확장
            int sz = qa.size();
            while(sz-- && !done){
                auto s = qa.front(); qa.pop();
                if(distB.count(s)){
                    answer = distA[s] + distB[s];
                    done = true;
                    break;
                }
                for(int i = 0; i < 6; i++){
                    auto t = s;
                    int times = 1 + (i/3)*2;
                    for(int k = 0; k < times; k++)
                        t = moveCube(i%3, t);

                    if(distB.count(t)){
                        answer = distA[s] + distB[t] + 1;
                        done = true;
                        break;
                    }
                    if(!distA.count(t)){
                        distA[t] = distA[s] + 1;
                        qa.push(t);
                    }
                }
            }
            if(done) break;

            // 한 단계씩 B 쪽 확장
            sz = qb.size();
            while(sz-- && !done){
                auto s = qb.front(); qb.pop();
                if(distA.count(s)){
                    answer = distA[s] + distB[s];
                    done = true;
                    break;
                }
                for(int i = 0; i < 6; i++){
                    auto t = s;
                    int times = 1 + (i/3)*2;
                    for(int k = 0; k < times; k++)
                        t = moveCube(i%3, t);

                    if(distA.count(t)){
                        answer = distA[t] + distB[s] + 1;
                        done = true;
                        break;
                    }
                    if(!distB.count(t)){
                        distB[t] = distB[s] + 1;
                        qb.push(t);
                    }
                }
            }
        }

        cout << answer << "\n";
    }

    return 0;
}
