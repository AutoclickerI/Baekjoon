# [Diamond V] Who wants to live forever? - 3406 

[문제 링크](https://www.acmicpc.net/problem/3406) 

### 성능 요약

메모리: 51820 KB, 시간: 276 ms

### 분류

분할 정복, 수학

### 제출 일자

2026년 3월 14일 23:48:26

### 문제 설명

<p>Digital physics is a set of ideas and hypotheses that revolve around the concept of computable universe. Maybe our universe is just a big program running on a Turing machine? Is the state of the universe finite? Will the life of the universe end? We can only theorize.</p>

<p>In order to help advance the current state of knowledge on digital physics, we ask you to consider a particular model of the universe (which we shall call Bitverse) and determine whether its life comes to a conclusion or continues evolving forever.</p>

<p>Bitverse consists of a single sequence of n bits (zeros or ones). The universe emerges as a particular sequence, in an event called the “Bit Bang”, and since then evolves in discrete steps. The rule is simple—to determine the next value of the i-th bit, look at the current value of the bits at positions i − 1 and i + 1 (if they exist; otherwise assume them to be 0). If you see exactly one 1, then the next value of the i-th bit is 1, otherwise it is 0. All the bits change at once, so the new values in the next state depend only on the values in the previous state. We consider the universe dead if it contains only zeros.</p>

<p>Given the state of the universe at the Bit Bang, answer the following fundamental question: will Bitverse live forever, or will it eventually die?</p>

### 입력 

 <p>The first line of the input contains the number of test cases T. The descriptions of the test cases follow:</p>

<p>Each test case is a string of at least 1 and at most 200 000 characters 0 or 1.</p>

### 출력 

 <p>Print the answers to the test cases in the order in which they appear in the input. For each test case, print LIVES if the universe lives forever, and DIES otherwise.</p>

