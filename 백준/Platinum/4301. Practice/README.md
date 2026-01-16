# [Platinum I] Practice - 4301 

[문제 링크](https://www.acmicpc.net/problem/4301) 

### 성능 요약

메모리: 110760 KB, 시간: 4096 ms

### 분류

수학, 통계학, 경사 하강법

### 제출 일자

2026년 1월 16일 10:10:05

### 문제 설명

<p>How much does winning ACM depend on practice?</p>

<p>We assume that p, the probability that a given team will win a given contest, is related to n, the number of practice problems solved by the team prior to the contest. This relationship is modelled by the logistic formula</p>

<pre>log(p/(1-p)) = a + b n ,</pre>

<p>for some a and b. Your job is to find a and b such that the formula most accurately reflects a set of observed results.</p>

<p>Each observation consists of n and w. n is the number of practice problems solved by some team prior to a contest, and w is 1 if the team wins the contest, 0 if it does not.</p>

<p>Given a, b, and n the formula above may be used to compute p, the estimated probability that w = 1. The likelihood of a particular observation is p if w = 1 and 1-p if w = 0; The likelihood of a set of observations is the product of the likelihoods of the individual observations.</p>

<p>You are to compute the maximum likelihood estimate for a and b. That is, the values of a and b for which the likelihood of a given set of observations is maximized.</p>

### 입력 

 <p>The input contains several test cases followed by a line contatining 0. Each test case begins with 1 < k ≤ 100, the number of observations that follow. Each observation consists of integers 0 ≤ n ≤ 100 and 0 ≤ w ≤ 1. The input will contain at least two distinct values of n and of w.</p>

### 출력 

 <p>For each test case, output a single line containing a and b, rounded to four digits to the right of the decimal.</p>

