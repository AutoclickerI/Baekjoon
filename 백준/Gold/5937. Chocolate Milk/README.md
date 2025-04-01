# [Gold III] Chocolate Milk - 5937 

[문제 링크](https://www.acmicpc.net/problem/5937) 

### 성능 요약

메모리: 199896 KB, 시간: 676 ms

### 분류

방향 비순환 그래프, 그래프 이론, 위상 정렬

### 제출 일자

2025년 4월 1일 22:36:07

### 문제 설명

<p>Farmer John's milk production and shipping system is an intricate one! He uses milking machines for his many cows to harvest the milk that then flows into pipes.</p>

<p>Each of these pipes connects a milking machine to a joint, where it might be joined by exactly one more pipe (the milk flowing through both pipes merges). The milk then flows through additional pipes (which all start and end at joints) until it reaches the long central pipe connecting to the distribution room.</p>

<p>The milk then goes through a reverse process of splitting at various joints until it is flows into milk tanks that are picked up and taken to market.</p>

<p>Farmer John notices that there is at most one way for milk to travel from one joint to any other joint. Furthermore, since Farmer John is an efficient man by nature, he has made sure that milk will flow through each and every pipe; in other words, no pipe is unneeded.</p>

<p>If we think of a milking machine, joint, or milk tank as a node, there are N (2 <= N <= 100,000) nodes in total (and N-1 pipes connecting them). The input describes each pipe as an ordered pair of nodes, A_i (1 <= A_i <= N) and B_i (1 <= B_i <= N; A_i < B_i) indicating milk flows from node A_i to node B_i. If there is no pipe coming in to A_i, it is a milking machine. Likewise, if no pipe goes out from B_i, it is a tank.</p>

<p>The demand of chocolate milk has skyrocketed in recent months, and Farmer John wants to install a chocolate inserter at one of the joints so he can create delicious chocolate milk for customers.</p>

<p>Being thrifty, Farmer John has only bought one chocolate inserter, so he wants to place it at a joint through which all the milk passes. He knows that such a joint exists.</p>

<p>Help Farmer John find all the possible places he can install the chocolate inserter.  (Note that Farmer John cannot install the chocolate inserter at the same location as a milking machine.)</p>

<p>As an example, consider a milking setup like this one:</p>

<pre>           1 ----+
                 |
                 v
           2 --> 4 --> 6 ------------------> 7 --> 8
                       ^                     |
                       |                     |
           3 --> 5 ----+                     + --> 9</pre>

<p>Visual inspection shows that the chocolate inserter can be installed at either joint 6 or 7, as all milk flows through those joints.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N: Line i+1 contains two space-separated integers that describe a pipe's connectivity: A_i and B_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..??: Integers, one per line and in ascending order, each denoting a possible joint at which to install the chocolate inserter.</li>
</ul>

<p> </p>

