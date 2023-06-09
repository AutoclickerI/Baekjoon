# [Platinum II] Quaternion inverse - 10909 

[문제 링크](https://www.acmicpc.net/problem/10909) 

### 성능 요약

메모리: 31620 KB, 시간: 656 ms

### 분류

분할 정복을 이용한 거듭제곱, 수학, 모듈로 곱셈 역원, 정수론

### 문제 설명

<p>사원수(Quaternion)는 복소수를 확장해 만든 수 체계이다. 사원수는 \(i^2 = j^2 = k^2 = ijk = -1\)을 만족하는 세 복소수 \(i\), \(j\), \(k\)를 이용해 표현되어 네 개의 실수 성분을 가지는데, 우리는 앞으로 아래 집합에 속하는 사원수만을 고려할 것이다. 이를 제한된 사원수라고 하자.</p>

<p>\[a + bi + cj + dk \left(a, b, c, d\text{는} 0 \text{이상} M \text{미만의 정수}\right)\]</p>

<p>다음으로 두 사원수의 곱셈에 관하여 생각해 보자. \(i\), \(j\), \(k\) 사이의 성질 때문에, 두 일반적인 사원수를 곱하면 아래와 같은 결과가 나온다.</p>

<p>\[(a_1 + b_1i + c_1j + d_1k) \times (a_2 + b_2i + c_2j + d_2k) = (a_1a_2 - b_1b_2 - c_1c_2 - d_1d_2) + (a_1b_2 + b_1a_2 + c_1d_2 - d_1c_2)i + (a_1c_2 - b_1d_2 + c_1a_2 + d_1b_2)j + (a_1d_2 + b_1c_2 - c_1b_2 + d_1a_2)k\]</p>

<p>우리는 두 제한된 사원수를 곱한 결과를 이 두 사원수를 일반적인 사원수로 취급하여 곱하였을 때의 결과에서 각 정수 성분을 \(M\)으로 나눈 나머지로 치환한 것으로 생각할 것이다. \(M\)과 제한된 사원수 \(A\)가 주어질 때, \(AB = 1\)이 되는 제한된 사원수 \(B\) 중 하나를 구하여라.</p>

### 입력 

 <p>첫 번째 줄에 자연수 \(M\)과 \(T\) (1 ≤ \(T\) ≤ 100,000)가 공백으로 구분되어 주어진다. \(M\)은 소수이다. (즉 약수가 1과 자기 자신밖에 없다.)</p>

<p>다음 \(T\)개의 줄의 각 줄에는 \(A\)를 나타내는 네 개의 정수 \(a\), \(b\), \(c\), \(d\) (0 ≤ \(a\), \(b\), \(c\), \(d\) < \(M\))가 공백으로 구분되어 주어지며, 이 경우 \(A = a + bi + cj + dk\)이다.</p>

<p>2 ≤ \(M\) ≤ 100,000인 입력이 주어진다.</p>

### 출력 

 <p>각 \(A\)가 주어질 때마다, \(AB = 1\)을 만족하는 \(B = a + bi + cj + dk\)들 중 하나를 나타내는 네 개의 정수 \(a\), \(b\), \(c\), \(d\)를 공백으로 구분하여 \(T\) 줄에 걸쳐 출력하면 된다. 만약 이런 \(B\)가 존재하지 않으면 0을 공백으로 구분하여 네 번 출력하면 된다.</p>

