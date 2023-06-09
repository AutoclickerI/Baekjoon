# [Gold V] 정렬하기 - 16219 

[문제 링크](https://www.acmicpc.net/problem/16219) 

### 성능 요약

메모리: 159748 KB, 시간: 764 ms

### 분류

많은 조건 분기

### 문제 설명

<p>종영이는 입력 데이터를 만들기 귀찮았다. 사실 문제를 생각하는 것 자체도 귀찮았다. 그래서 IOI 2015의 "정렬하기" 문제 ( acmicpc.net/problem/10924 )를 변형해 입력 데이터를 재탕하기로 했다! 종영이의 문제를 해결하자. 종영이의 문제는 다음과 같다.</p>

<hr>
<p>에르맥과 아이잔은 길이 N의 수열 S를 가지고 게임을 하려고 한다. 수열 S에는 0부터 N-1까지의 정수가 한 번씩만 등장한다. 이 게임은 수열을 오름차순으로 정렬하는 게임으로, 아이잔은 수열을 정렬하려고 하고, 에르맥은 정렬되지 않게 하려고 하며, 불가피할 경우 최대한 오랫동안 정렬되지 않게 하는 것이 목표이다. </p>

<p>한 게임에서, 각 라운드마다 에르맥이 두 수를 정해 서로의 위치를 바꾸고, 다음에 아이잔이 두 수를 정해 서로의 위치를 바꾼다. 에르맥과 아이잔 모두 같은 수를 정해 위치가 바뀌지 않게 할 수도 있다. 해당 라운드에서 수열이 오름차순으로 정렬되면 게임은 끝이 나며, 처음부터 정렬되어 있는 경우 필요한 라운드의 수는 0이다.</p>

<p>게임을 여러 번 하기 위해, 에르맥과 아이잔은 수열 S에 대해, S를 M번 변형하여 게임을 하려고 한다. 길이 M의 배열 X와 Y가 있을 때, 게임의 번호를 게임을 한 순서대로 0부터 M-1까지라 하면, i번째 게임을 시작하기 전에, i-1번째 게임을 시작했던 순간의 수열에서 X[i]번째 위치의 수와 Y[i]번째 위치의 수를 바꾼다. 그 후 새로운 수열을 게임에서 사용한다. -1번째 게임을 시작했던 순간의 수열은 편의상 S라고 정의하자.</p>

<p>각 게임에 대하여, 아이잔이 특정 라운드가 지난 후 반드시 승리하는지와, 승리한다면, 필요한 라운드 수의 최솟값을 구해야 한다.</p>

### 입력 

 <p>첫 줄에 N이 주어진다. (1 ≤ N ≤ 2 × 10<sup>5</sup>)</p>

<p>둘째 줄에 수열 S가 N개의 수가 공백으로 구분되어 주어진다. (수열 S는 0부터 N-1까지의 정수가 한 번씩 등장하는 수열이다.)</p>

<p>세번째 줄에 M이 주어진다. (1 ≤ M ≤ 6 × 10<sup>5</sup>)</p>

<p>M개의 줄에 걸쳐, X[i]와 Y[i]가 공백으로 구분되어 주어진다. (0 ≤ X[i], Y[i] < N)</p>

### 출력 

 <p>M개의 게임에 대해, 각 게임이 일어난 순서대로, 게임이 무한히 진행 가능하다면 -1, 아니면 필요한 최소 라운드의 수를 공백으로 구분되어 출력한다.</p>

