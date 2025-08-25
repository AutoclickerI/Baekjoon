#include "aplusb.h"

std::vector<int> Al;
std::vector<int> Bl;

void initialize(std::vector<int> A, std::vector<int> B) {
  Al = A;
  Bl = B;
  return;
}

int answer_question(int i, int j) {
  return Al[i]+Bl[j];
}
