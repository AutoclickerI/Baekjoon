# [Silver V] Winning Wagers - 34303 

[문제 링크](https://www.acmicpc.net/problem/34303) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 확률론

### 제출 일자

2025년 9월 13일 07:49:45

### 문제 설명

<p>You and your friend finish the Physics I studio early one day. After completing an invigorating set of rotational motion problems, you decide to make some wagers based on event-driven probability (instead of getting a head-start on the homework for that week).</p>

<p>After rummaging through the lockers and desks in the studio room (with permission from the TAs, of course), you and your friend were able to gather the following probability items: a coin, an six-sided die, and a standard deck of $52$ cards.</p>

<p>You and your friend decide on the following rules for the friendly competition: a wager must consist of a series of discrete events from at least one of the probability items. Each probability item has <strong>only one</strong> discrete event associated with it:</p>

<ul>
	<li><code>COIN</code>: Obtaining either a "heads" or "tails" on a single flip.</li>
	<li><code>DIE</code>: Rolling a particular number ($1$-$6$) on the six-sided die.</li>
	<li><code>CARDS</code>: Drawing one particular card out of the $52$ card deck <strong>with</strong> replacement.</li>
</ul>

<p>Your friend will be offering you a wager. If you win the wager, your friend will give you $W$ dollars. If you lose, you'll need to pay your friend $L$ dollars.</p>

<p>For you to win the wager, you'll need to guess the outcome of each discrete event <strong>correctly</strong>. For example, if your friend offers you a wager that consists of flipping the coin, rolling the die, and drawing from the deck, you'll win <strong>only</strong> if you correctly guess which side the coin landed on, correctly guess which number was rolled on the die, and correctly guess the exact suit and face value of the card that was chosen. If you guess any outcome incorrectly, you'll lose the wager.</p>

<p>Your friend states the wager, and $L$ (the amount of money that you'll need to pay if you lose). You need to calculate a value for $W$ (the amount of money that your friend will pay you if you win the wager) such that the amount you win on average is zero.</p>

### 입력 

 <p>The first line of input is an integer, $1 \leq N \leq 8$, representing the number of discrete events composing the wager.</p>

<p>The second line of input is a space-separated list of $N$ probability item strings, each representing it's corresponding discrete event.</p>

<p>The third and final line of input will be an integer, $1 \leq L \leq 10^4$, corresponding to the amount of money that you'll need to pay your friend if you lose.</p>

### 출력 

 <p>Output a single integer $W$ (the amount of money that your friend will pay you if you win the wager) such that the amount you win on average is zero.</p>

