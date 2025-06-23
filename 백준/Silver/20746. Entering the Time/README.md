# [Silver V] Entering the Time - 20746 

[문제 링크](https://www.acmicpc.net/problem/20746) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

많은 조건 분기, 다이나믹 프로그래밍, 그리디 알고리즘

### 제출 일자

2025년 6월 23일 23:50:48

### 문제 설명

<p>Arghs! Yet again, all the clocks in Petra's home show the wrong time due to a power outage that occurred while she was sleeping. This means she has to spend her day resetting all the clocks to the correct time. Now, you might not consider this a big deal. After all, how many clocks does any single household really have? Well, Petra just so happens to be a collector of clocks. She literally has hundreds of clocks -- and that is just in her bedroom! Thus, it is understandable that she does not look forward to all this resetting.</p>

<p>You, as her friend, would prefer if she did not need to spend her entire day resetting all her clocks. Especially since this means she would not have any time to play with you! If only you could construct some automated way of entering the correct time into all the clocks, perhaps through some kind of computer code...</p>

<p>A-ha, of course! You can write a program to determine how to set the correct time as quickly as possible!</p>

<p>Each clock has a display of $4$ digits: two are used to display the hour (between <code>00</code> and <code>23</code>), and two are used to display the minute (between <code>00</code> and <code>59</code>). The time can be changed by selecting a digit and either decreasing or increasing by $1$. Decreasing a digit that is $0$, it is turned into $9$, and increasing a digit $9$ turns it into $0$. However, the clock can not display invalid times. This means that at any given time, the hour must be between <code>00</code> and <code>23</code> and the minute between <code>00</code> and <code>59</code>.</p>

<p>Write a program that, given the original time of a clock and the current time, determines how to set the clock correctly.</p>

### 입력 

 <p>The input consists:</p>

<ul>
	<li>one line with the time that the clock is currently set to.</li>
	<li>one line with the current time.</li>
</ul>

<p>Each time has the format <code>hh:mm</code>, where <code>hh</code> is a two-digit number between <code>00</code> and <code>23</code>, and <code>mm</code> is a two-digit number between <code>00</code> and <code>59</code>.</p>

### 출력 

 <p>The first line contains the number of different times seen on the clock when setting it correctly. Then for each time output it on the same format as above <code>hh:mm</code> on a separate line. Include both the original time and the final time.</p>

