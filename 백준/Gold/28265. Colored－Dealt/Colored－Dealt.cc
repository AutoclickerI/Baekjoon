#include <string>
#include "colored_dealt.h"

using namespace std;

string guess(int N) {
	string s = "", ans = "";
	for (int i = 0; i < N; i++)
		s += "R";
	int score = design(s), tmp, check;
	check = score;
	for (int i = 0; i < N - 1; i++) {
		s[i] = 'B';
		tmp = design(s);
		switch (tmp - score) {
		case 0:
			ans += "B";
			check -= 3;
			break;
		case 1:
			ans += "G";
			check -= 2;
			break;
		case 2:
			ans += "R";
			check -= 1;
			break;
		}
		score = tmp;
	}
	switch (check) {
	case 1:
		ans += "R";
		break;
	case 2:
		ans += "G";
		break;
	case 3:
		ans += "B";
		break;
	}
	return ans;
}
