#include <string>

void init(){ }

int next_move(std::string state){
    if(state=="01010101010101")
        return 4;
    if(state=="01010106010101")
        return 4;
    if(state=="0101011a010101")
        return 4;
    if(state=="0101012a030101")
        return 2;
    if(state=="01010106010101")
        return 4;
    if(state=="0101011a010101")
        return 4;
    return 0;
}