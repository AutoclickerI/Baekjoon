# [Diamond V] Food Festival - 17321 

[문제 링크](https://www.acmicpc.net/problem/17321) 

### 성능 요약

메모리: 135688 KB, 시간: 2176 ms

### 분류

벨만–포드, 최대 유량, 그래프 이론, 최소 비용 최대 유량, 최단 경로

### 제출 일자

2026년 4월 24일 15:25:01

### 문제 설명

<p>To welcome students from all across the nation, City CZ is specially hosting a grand food festival.</p>

<p>Being a food fanatic who loves to try new flavors, little M obviously does not want to miss this feast. Going there, he quickly was able to sample lots of the festival's great foods. Yet, it is still hard to satisfy the appetite of a true gastronome, even if the dishes are very tasty and the kitchen is very efficient. Little M still thinks that not having dishes which are already on someone else's table is an unbearable feeling. So, little M started to investigate issues relating to the order in which dishes are prepared, hoping to create an efficient system that minimizes the waiting time of students.</p>

<p>Little M noticed that the food festival contains <var>n</var> varieties of delicacies. When ordering each time, each student can select one of these varieties. There are a total of <var>m</var> chefs to prepare these dishes. After all of the students have ordered, the tasks of preparing the dishes will assigned to each of the chefs. Then, each chef will simultaneously start to cook. The chefs will follow the required order when they prepare the dishes, and each time can only make a portion for one person.</p>

<p>Other than this, little M also made an interesting observation — even though these <var>m</var> chefs all know how to fully prepare all <var>n</var> varieties of delicacies, different chefs may require different amounts of time to prepare the same dish. He numbered the types of delicacies from 1 to <var>n</var>, and the chefs from 1 to <var>m</var>, denoting the time it takes for <var>j</var>-th chef to prepare the <var>i</var>-th delicacy as <var>t<sub>i, j</sub></var>.</p>

<p>Little M will consider each student's <i>waiting time</i> to be from when <i>all chefs</i> start to cook to when their own dish is fully prepared. In other words, if a student's ordered dish is the <var>k</var>-th delicacy to be prepared by some chef, then their waiting time is the sum of the preparation times of the first <var>k</var> dishes that this chef prepares. The <i>total waiting time</i> is the sum of the waiting times among all of the students.</p>

<p>Now, little M has the orders of each and every student — there are <var>p<sub>i</sub></var> students who ordered the <var>i</var>-th type of delicacy (for <var>i</var> = 1, 2, …, <var>n</var>). He would like to know the minimum possible total waiting time.</p>

### 입력 

 <p>The first line of input contains two positive integers <var>n</var> and <var>m</var>, representing the number of varieties of delicacies and chefs, respectively.</p>

<p>Line 2 contains <var>n</var> positive integers <var>p</var><sub>1</sub>, <var>p</var><sub>2</sub>, …, <var>p<sub>n</sub></var>, where <var>p<sub>i</sub></var> is the number of students who ordered the <var>i</var>-th delicacy.</p>

<p>For the following <var>n</var> lines, each line contains <var>m</var> nonnegative integers. The <var>j</var>-th integer on the <var>i</var>-th line will be <var>t<sub>i, j</sub></var>, the time it takes for the <var>j</var>-th chef to prepare the <var>i</var>-th delicacy.</p>

<p>All adjacent numbers on the same line will be separated by a single space, and there will be no trailing spaces on any line.</p>

### 출력 

 <p>Output one line containing a single integer, the smallest possible total waiting time.</p>

