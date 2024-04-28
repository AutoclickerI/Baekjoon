#include "ethereum.h"
#include <stdio.h>

excinfo GetExchangePrice() {
	excinfo A=Exchange(100000000);  
	excinfo B=Exchange(99999999);  
	excinfo ret;
	long long det=A.BTC*B.ETH-A.ETH*B.BTC;
	ret.BTC=(B.ETH*100000000-A.ETH*99999999)/det;
	ret.ETH=(A.BTC*99999999-B.BTC*100000000)/det;
	return ret;
}
