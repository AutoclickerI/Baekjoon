from bisect import*
print(bisect_right([7,17,19,23,29,31,43,47,59,61,67,71,83,97,107,109,113,131,149,151,163,167,179,181,191,193,199,223,227,229,233,257,263,269,283,307,311,313,337,347,359,367,379,383,389,419,431,433,439,443,461,467,479,487,491,499,503,509,523,541,563,571,577,587,593,599,619,631,647,659,683,701,709,719,727,743,787,811,821,823,827,839,857,863,883,887,911,919,937,941,947,953,971,977,983,991,1019,1021,1033,1039,1051,1063,1069,1087,1091,1097,1103,1109,1123,1151,1153,1163,1171,1181,1187,1193,1217,1223,1229,1259,1279,1283,1291,1297,1301,1303,1307,1319,1327,1367,1381,1399,1427,1429,1433,1439,1447,1471,1487,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1607,1619,1621,1663,1667,1697,1709,1741,1759,1777,1783,1787,1789,1811,1823,1847,1861,1867,1871,1873,1907,1913,1949,1979,1999,2003,2017,2027,2029,2039,2063,2069,2083,2099,2111,2113,2137,2141,2143,2153,2179,2203,2207,2221,2239,2243,2251,2267,2269,2273,2297,2309,2339,2341,2347,2351,2371,2383,2389,2399,2411,2417,2423,2447,2459,2473,2539,2543,2549,2579,2593,2617,2621,2633,2657,2663,2671,2687,2699,2707,2711,2713,2719,2731,2741,2753,2767,2777,2789,2803,2819,2833,2843,2851,2861,2879,2887,2897,2903,2909,2927,2939,2963,2971,2999,3011,3019,3023,3067,3079,3083,3119,3137,3163,3167,3203,3221,3251,3257,3259,3271,3299,3301,3307,3313,3323,3331,3343,3347,3359,3371,3389,3391,3407,3433,3461,3463,3467,3469,3511,3527,3539,3547,3559,3571,3581,3593,3607,3617,3623,3631,3643,3659,3673,3701,3709,3719,3727,3767,3779,3803,3821,3833,3847,3863,3907,3911,3923,3943,3947,3967,3989,4007,4019,4027,4051,4057,4073,4079,4091,4099,4111,4127,4139,4153,4177,4211,4217,4219,4229,4231,4243,4259,4261,4271,4283,4327,4337,4339,4349,4363,4391,4421,4423,4447,4451,4457,4463,4523,4547,4567,4583,4591,4603,4639,4643,4651,4673,4679,4691,4703,4723,4751,4759,4783,4787,4793,4799,4817,4871,4919,4931,4937,4943,4951,4967,4987,5003,5021,5039,5059,5087,5099,5107,5147,5153,5167,5179,5189,5227,5231,5233,5273,5279,5297,5303,5309,5323,5347,5351,5381,5387,5393,5399,5417,5419,5431,5479,5483,5501,5503,5507,5519,5527,5531,5563,5581,5591,5623,5639,5651,5657,5659,5669,5683,5701,5737,5741,5743,5749,5779,5783,5807,5821,5827,5839,5843,5857,5861,5867,5869,5879,5897,5903,5923,5927,5939,5981,5987,6011,6029,6043,6047,6067,6073,6113,6131,6143,6199,6211,6217,6221,6247,6257,6263,6269,6287,6301,6311,6323,6337,6343,6353,6359,6367,6389,6473,6551,6553,6563,6571,6599,6619,6659,6661,6673,6679,6691,6701,6703,6709,6719,6737,6779,6793,6803,6823,6827,6829,6833,6857,6863,6869,6871,6883,6899,6911,6947,6949,6959,6967,6971,6977,6983,6991,7019,7057,7069,7079,7103,7109,7159,7177,7187,7193,7207,7219,7229,7243,7247,7283,7307,7309,7349,7393,7411,7433,7451,7457,7459,7487,7499,7507,7523,7541,7547,7559,7577,7583,7591,7607,7639,7643,7673,7687,7691,7699,7703,7727,7753,7759,7793,7817,7823,7829,7867,7873,7879,7883,7901,7907,7919,7927,7937,7949,7951,7963,8017,8039,8059,8069,8087,8123,8147,8171,8179,8219,8231,8233,8243,8263,8269,8273,8287,8291,8297,8311,8353,8363,8377,8389,8423,8429,8431,8443,8447,8467,8501,8513,8537,8543,8563,8623,8627,8647,8663,8669,8699,8707,8713,8719,8731,8741,8747,8753,8783,8807,8819,8821,8831,8839,8861,8863,8867,8887,8951,8963,8971,8999,9011,9029,9043,9059,9067,9103,9109,9137,9187,9199,9203,9221,9227,9239,9257,9311,9319,9323,9341,9343,9371,9377,9391,9421,9431,9461,9467,9473,9479,9491,9497,9539,9547,9587,9623,9629,9631,9643,9697,9719,9739,9743,9749,9767,9781,9787,9791,9803,9811,9817,9829,9833,9839,9851,9857,9871,9883,9887,9907,9923,9931,9949,9967],int(input())))