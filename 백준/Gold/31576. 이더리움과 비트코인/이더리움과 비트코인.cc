#include "ethereum.h"
#include <stdio.h>
#include <numeric>

excinfo GetExchangePrice() {
	excinfo A = Exchange(100000000);
    excinfo B = Exchange(99999999);
    excinfo ret;
    __int128 k1=100000000,k2=99999999;
    if (A.BTC>B.BTC){
        ret.BTC=A.BTC;ret.ETH=A.ETH;
        A.BTC=B.BTC;A.ETH=B.ETH;
        B.BTC=ret.BTC;B.ETH=ret.ETH;
        k1=99999999;
        k2=100000000;
    }
    __int128 btc1=A.BTC,eth1=A.ETH,btc2=B.BTC,eth2=B.ETH;
    if(A.BTC){
        __int128 lcm=A.BTC*B.BTC/std::gcd(A.BTC,B.BTC),tmp;
        tmp=k2;
        btc2=lcm;
        eth2=A.ETH*lcm/A.BTC;
        k2=k1*lcm/A.BTC;
        btc1=lcm;
        eth1=B.ETH*lcm/B.BTC;
        k1=tmp*lcm/B.BTC;
        btc2-=btc1;
        eth2-=eth1;
        k2-=k1;
        k2/=eth2;
        eth2=1;
        k1-=k2*eth1;
        eth1=0;
        k1/=btc1;
        btc1=1;
        ret.BTC=k1;
        ret.ETH=k2;
        return ret;
    }
    k1/=eth1;
    eth1=1;
    k2-=eth2*k1;
    eth2=0;
    k2/=btc2;
    btc2=1;
    ret.BTC=k2;
    ret.ETH=k1;
    return ret;
}
