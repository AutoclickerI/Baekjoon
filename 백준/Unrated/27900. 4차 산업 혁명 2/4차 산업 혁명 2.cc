#include <string>

void init(){ }

int next_move(std::string state){
    if(state=="01010101010101")
        return 4;
    if(state=="01010106010101")
        return 4;
    if(state=="0101011a010101")
        return 4;
    if(state=="0101012a030101") // +2
        return 2;
    if(state=="0102012a070101") // +1
        return 1;
    if(state=="0202032a070101") // +1
        return 3;
    if(state=="02020d2a070101") // +1
        return 3;
    if(state=="0602152a070101") // +1
        return 1;
    if(state=="0a06152a070101") // +1
        return 3;
    if(state=="0a06256a070101") // +1
        return 1;
    if(state=="120e256a070101") // +1
        return 2;
    if(state=="1236256a070101") // +1
        return 1;
    if(state=="6236256a070101") // +1
        return 2;
    if(state=="6256256a070301") // +1
        return 6;
    if(state=="6256256a070d01") // +1
        return 5;
    if(state=="6256256a1b0d01") // +1
        return 5;
    if(state=="6256256a6b0d01") // +1
        return 7;
    if(state=="6256656a6b0d02") // +1
        return 7;
    if(state=="6256656a6b0d0c") // +1
        return 7;
    if(state=="6256656a6b0d34") // +1
        return 7;
    if(state=="6256656a6b1d54") // +1
        return 6;
    return 0;
}