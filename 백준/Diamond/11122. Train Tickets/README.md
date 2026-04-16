# [Diamond V] Train Tickets - 11122 

[문제 링크](https://www.acmicpc.net/problem/11122) 

### 성능 요약

메모리: 112588 KB, 시간: 220 ms

### 분류

애드 혹, 최대 유량, 최소 비용 최대 유량, 그래프 이론

### 제출 일자

2026년 4월 16일 16:13:27

### 문제 설명

<p>Tor Gunnar is a huge fan of trains. All his life, he’s been running around at home yelling ”Toot Toot”. So when he recently found out about a job opening at a local train company, he immediately applied. Tor Gunnar, having studied really hard to reach such opportunities, got the job. It was the happiest moment of his life! To his great dissappointment, though, he discovered that the contract said nothing about riding trains all day. He is now assigned to the IT department, and is supposed to help write a new ticket management system. The part he is supposed to write, is an algorithm for distributing tickets among the different possible travels along a train route.</p>

<p>Tor Gunnar comes from a strange country. In addition to speaking a language even he himself doesn’t understand, the countrys government has pushed through some weird laws that influences how train tickets are sold. This means that the price for travelling from station A to station B is predetermined. Also, everytime you sell tickets for a given trip, you’ll know the exact demand for travelling between each pair of cities. What more, the government is allowed to set aside some tickets for their own usage (these are free of charge).</p>

<p>One train trip consists of a series of stations. It is possible to travel from station A to B as long as A precedes B in the station list. Each train has a given capacity, and there can never be more than this amount of passengers in between two adjacent stations.</p>

<p>Tor Gunnar is completely puzzled, and desperately needs your help. Write a program that helps him figure out the best ticket distribution.</p>

### 입력 

 <p>The first line of input contains a single number T, the number of test cases to follow. Each test case begins with a line containing two numbers, N and P, the number of stations in the case and the capacity of the train, respectively. Then follow N − 1 lines, giving the ticket prices, C<sub>ij</sub>. The i-th of these N lines contain N − i numbers. The j-th number of the i-th line is the cost of a ticket from station i to station i + j. The next N − 1 lines give the demand for tickets for each pair of stations, D<sub>ij</sub>, in the same format as the prices. Another N − 1 lines in the same format follow these, statin the number of tickets set aside for the government officials, O<sub>ij</sub>.</p>

<ul>
	<li>0 < T ≤ 100</li>
	<li>3 ≤ N ≤ 16</li>
	<li>0 < P ≤ 200</li>
	<li>0 < C<sub>ij</sub> ≤ 1000</li>
	<li>0 ≤ D<sub>ij</sub> ≤ 250</li>
	<li>0 ≤ O<sub>ij</sub> ≤ 20</li>
	<li>A train trip goes from station 1 to station N.</li>
	<li>Keep in mind that the passenger count including the government officials cannot be more than the capacity.</li>
	<li>You are not allowed to overbook the train.</li>
	<li>The government will never overbook your train using their ”free” tickets.</li>
</ul>

### 출력 

 <p>For each test case, output a single number on a line by itself. The number should equal the maximum possible income from the train trip.</p>

