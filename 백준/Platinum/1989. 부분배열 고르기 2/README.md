# [Platinum V] 부분배열 고르기 2 - 1989 

[문제 링크](https://www.acmicpc.net/problem/1989) 

### 성능 요약

메모리: 320648 KB, 시간: 704 ms

### 분류

자료 구조, 분할 정복, 누적 합, 세그먼트 트리, 스택

### 제출 일자

2025년 4월 1일 22:10:42

### 문제 설명

<p>크기가 N(1 ≤ N ≤ 100,000)인 1차원 배열 A[1], …, A[N]이 있다. 어떤 i, j(1 ≤ i ≤ j ≤ N)에 대한 점수는, (A[i] + … + A[j]) × min{A[i], …, A[j]}가 된다. 즉, i부터 j까지의 합에 i부터 j까지의 최솟값을 곱한 것이 점수가 된다.</p>

<p>배열이 주어졌을 때, 최대의 점수를 갖는 부분배열을 골라내는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정수 N이 주어진다. 다음 줄에는 A[1], …, A[N]을 나타내는 정수들이 주어진다. 각각의 정수들은 음이 아닌 값을 가지며, 1,000,000을 넘지 않는다.</p>

### 출력 

 <p>첫째 줄에 최대 점수를 출력하고, 둘째 줄에 그 구간의 시작 위치(i)와 끝 위치(j)를 출력한다.</p>

