# [Bronze I] Coatis and Owls - 33231 

[문제 링크](https://acmicpc.net/problem/33231) 

### 선택한 제출

[제출 89696153](https://acmicpc.net/source/89696153) · Python 3 · 389 B · Coatis and Owls.py

### 성능 요약

메모리: 73596 KB, 시간: 292 ms

### 분류

수학, 구현, 시뮬레이션

### 제출 일자

2025년 2월 7일 13:00:43

### 문제 설명

<p>The coatis and owls have been at war for a long time already. They are preparing for battle, but given the pandemic, they also want to comply to social distancing. Therefore, they decide to do a digital battle instead, by playing the game Furious Pikemen Combat (FPC) against each other.  % Or: Fighting Pikeman Championship</p>

<p>The game features a one-dimensional battlefield. Both players control an <em>army</em>, each consisting of multiple <em>squads</em> of pikemen. The coati army is positioned on the left and the owl army is positioned on the right. During the game, the coati army walks to the right while the owl army walks to the left. When two enemy squads meet, they fight until one of the squads is completely defeated. Since all pikemen are equal in strength, the smaller squad will lose all of its pikemen. The winning squad will lose a number of pikemen depending on the size of the winning squad ($w$) and the size of the losing squad ($l$), equal to $\left\lceil l^2 / w \right\rceil$ (where $\lceil x \rceil$ denotes rounding $x$ up to the nearest integer, or ceiling). If two squads are equal in size, they will fight until both squads are annihilated.</p>

<p>Consider the first sample input as an example. The two squads controlled by the coatis (of $20$ pikemen) walk to the right and the squad controlled by the owls (of $33$ pikemen) walks to the left. When the right-most coati squad meets the owl squad, the coati squad is completely destroyed, while the owl squad loses $\left\lceil 20^2/33 \right\rceil = 13$ pikemen. In other words, the owl squad has $20$ pikemen left. The single remaining squad for both players then consists of exactly $20$ pikemen, so both squads will be annihilated, resulting in a stalemate.</p>

<p>Calculate who wins this digital battle of FPC, and how many pikemen the army of the winning player has left after the battle.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>A line with two integers $n$ and $m$ ($1\leq n,m\leq 2\cdot 10^5$), the number of squads controlled by the coatis and the owls, respectively.</li>
	<li>A line with $n + m$ integers $a$ ($1 \leq a \leq 10^4$), where each $a$ indicates the size of one squad of pikemen.</li>
</ul>

### 출력 

 <p>If all pikemen from both armies are defeated, output "<code>stalemate</code>".</p>

<p>If one player wins the battle, output:</p>

<ul>
	<li>A line containing either "<code>coatis</code>" if the coatis win the battle, or "<code>owls</code>" if the owls win the battle.</li>
	<li>A line with the number of pikemen remaining in the army of the winning player.</li>
</ul>

