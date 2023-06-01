#include <iostream>
#include <vector>
using namespace std;

int p, q,r=0;
string st;
vector<string> l;
void actionA(int y, int x, char s) {
	l[y][x] = l[y][x + 3] = l[y + 1][x] = l[y + 1][x + 1] = l[y + 1][x + 2] = l[y + 1][x + 3] = s;
}
void actionB(int y, int x, char s) {
	l[y][x] = l[y][x + 1] = s;
}
bool checkactionA(int y, int x) {
	if ((x+3 > q - 1) || (y+1 > p - 1))
		return false;
	else
		return (l[y][x] == l[y][x + 3]) && (l[y][x + 3] == l[y + 1][x]) && (l[y + 1][x] == l[y + 1][x + 1]) && (l[y + 1][x + 1] == l[y + 1][x + 2]) && (l[y + 1][x + 2] == l[y + 1][x + 3]) && (l[y + 1][x + 3] == 'X');
}
bool checkactionB(int y, int x) {
	if ((x+1 > q - 1) || (y > p - 1))
		return false;
	else
		return (l[y][x] == l[y][x + 1]) && (l[y][x + 1] == 'X');
}
void DFS(int y, int x) {
	if (y > r)r = y;
	if (y > p - 1||r-y>1) throw int(1);
	if (x > q - 1) {
		DFS(y + 1, 0);
		return;
	}
	if (l[y][x] != 'X')
		DFS(y, x + 1);
	else {
		if (checkactionA(y, x)) {
			actionA(y, x, 'A');
			DFS(y, x + 1);
			actionA(y, x, 'X');
		}
		if (checkactionB(y, x)) {
			actionB(y, x, 'B');
			DFS(y, x + 2);
			actionB(y, x, 'X');
		}
	}
}

int main() {
	
	cin >> p >> q;
	for (int i = 0; i < p; i++) {
		cin >> st;
		l.push_back(st);
	}
	try { 
		DFS(0, 0);
	}
	catch (...) {};
	bool flag = true;
	for (int i = 0; i < l.size(); i++) {
		for (int j = 0; j < l[i].size(); j++)
			if (l[i][j] == 'X')
				flag = false;
	}
	if (flag) {
		for (int i = 0; i < l.size(); i++) {
			for (int j = 0; j < l[i].size(); j++)
				cout << l[i][j];
			cout << endl;
		}
	}
	else cout << -1;

}