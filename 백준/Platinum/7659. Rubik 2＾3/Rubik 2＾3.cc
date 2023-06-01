#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

string move(const int n, const string& cube) {
	string b = cube;
	int n1, n2, n3;
	switch (n) {
	case 0:
		n1 = b[1]; n2 = b[3]; n3 = b[12];
		b[1] = b[22];
		b[3] = b[20];
		b[20] = b[19];
		b[22] = b[17];
		b[17] = b[5];
		b[19] = b[7];
		b[5] = n1;
		b[7] = n2;

		b[12] = b[13];
		b[13] = b[15];
		b[15] = b[14];
		b[14] = n3;
		break;

	case 1:
		n1 = b[4]; n2 = b[5]; n3 = b[0];
		b[4] = b[8];
		b[5] = b[9];
		b[8] = b[20];
		b[9] = b[21];
		b[20] = b[12];
		b[21] = b[13];
		b[12] = n1;
		b[13] = n2;

		b[0] = b[1];
		b[1] = b[3];
		b[3] = b[2];
		b[2] = n3;
		break;

	default:
		n2 = b[2]; n1 = b[3]; n3 = b[4];
		b[2] = b[12];
		b[3] = b[14];
		b[14] = b[16];
		b[12] = b[17];
		b[16] = b[9];
		b[17] = b[11];
		b[9] = n1;
		b[11] = n2;

		b[4] = b[5];
		b[5] = b[7];
		b[7] = b[6];
		b[6] = n3;
		break;
	}
	return b;
}

int main() {

	while (true) {
		vector<string> input(6);
		for (int i = 0; i < 6; i++)
			cin >> input[i];

		if (input[0][2] == '.') break;

		string cube = "";

		int arr[6][2] = { {0,2}, {2,2}, {2,0}, {2,4}, {4,2}, {2,6} };

		for (int i = 0; i < 6; i++) {
			int p = arr[i][0], q = arr[i][1];
			for (int j = 0; j < 2; j++)
				for (int k = 0; k < 2; k++)
					cube += input[p + j][q + k];
		}

		string cube_end = cube;
		cube_end[16] = cube_end[17] = cube_end[19] = cube_end[18];
		cube_end[20] = cube_end[21] = cube_end[22] = cube_end[23];
		cube_end[8] = cube_end[9] = cube_end[11] = cube_end[10];

		int corners[7][3] = { {2,9,4},{3,5,12},{1,13,20},{0,8,21},{6,11,16},{7,17,14},{19,15,22} };
		int per[6][3] = { {0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,1,0},{2,0,1} };
		for (int i = 0; i < 7; i++) {
			for (int j = 0; j < 6; j++) {
				char p = cube[corners[i][per[j][0]]], q = cube[corners[i][per[j][1]]], r = cube[corners[i][per[j][2]]];
				if (p == cube[18] && q == cube[23])
					cube_end[12] = cube_end[13] = cube_end[14] = cube_end[15] = r;
				if (p == cube[10] && q == cube[23])
					cube_end[0] = cube_end[1] = cube_end[2] = cube_end[3] = r;
				if (p == cube[10] && q == cube[18])
					cube_end[4] = cube_end[5] = cube_end[6] = cube_end[7] = r;
			}
		}

		map<string, string> sol_start;
		map<string, string> sol_end;
		queue<string> cub_start;
		queue<string> cub_end;
		string XYZ = "XYZ";
		sol_start[cube] = "";
		cub_start.push(cube);
		sol_end[cube] = "";
		cub_end.push(cube_end);

		bool conti = true;

		while (conti) {
			const string& b = cub_start.front();

			for (int i = 0; i < 3; i++) {
				string tmp = move(i, b);

				if (sol_start.find(tmp) == sol_start.end()) {
					sol_start[tmp] = sol_start[b] + XYZ[i];
					cub_start.push(tmp);
				}
			}
			cub_start.pop();

			const string& e = cub_end.front();
			for (int i = 0; i < 3; i++) {
				string tmp = move(i, e);

				if (sol_start.find(tmp) != sol_start.end()) {
					reverse(sol_end[e].begin(), sol_end[e].end());
					cout << (*sol_start.find(tmp)).second + XYZ[i] + XYZ[i] + XYZ[i] + sol_end[e] << endl;
					conti = false;
					break;
				}

				if (sol_end.find(tmp) == sol_end.end()) {
					sol_end[tmp] = sol_end[e] + XYZ[i] + XYZ[i] + XYZ[i];
					cub_end.push(tmp);
				}
			}
			cub_end.pop();
		}
	}
}