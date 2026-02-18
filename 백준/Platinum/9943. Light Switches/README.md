# [Platinum V] Light Switches - 9943 

[문제 링크](https://www.acmicpc.net/problem/9943) 

### 성능 요약

메모리: 39700 KB, 시간: 48 ms

### 분류

수학, 정수론, 백트래킹, 소수 판정, 소인수분해, 폴라드 로, 밀러–라빈 소수 판별법

### 제출 일자

2026년 2월 18일 14:38:22

### 문제 설명

<p>You are given a string of synchronized blinking lights with N bulbs. This string of lights is interesting in that instead of blinking on and off in unison, they follow a very specific pattern. Assume that at time t = 0 all bulbs are off. At each subsequent (integral) time t, bulbs toggle from on to off or off to on depending on their current configuration. When a bulb will toggle on or off depends on its position from the beginning of the string. If its position is a multiple of time t, it will toggle. So at time t = 1 all bulbs will toggle on (1, 2, 3, 4, etc.). At time t= 2 only even numbered bulbs (2, 4, 6, 8, etc.) will toggle again. At time t = 3 every third bulb (3, 6, 9, 12, etc.)toggles. This continues up to time t = N, at which point all bulbs are reset to off and the blinking pattern restartsat time t = N+1. (Thus time t = N+1 is viewed as equivalent to time t = 1: all bulbs are toggled on.)</p>

<p>Quality Control is having a hard time verifying that the bulbs are turning on and off at the appropriate times. Your team has been asked to write a verification program that can be given the number of bulbs N on the strand, a particular time t, and bulb position b, then determines if that bulb is on or off at time t + epsilon. In other words, if the bulb is on at time t + epsilon, then the bulb either toggled on at time t or was already on at time t.</p>

<p>The following limits hold for n, t, and b:</p>

<ul>
	<li>3 ≤ N < 2<sup>54</sup></li>
	<li>1 ≤ t, b < 2<sup>54</sup></li>
	<li>b ≤ N</li>
</ul>

<p>[The judge’s largest test case involves 17-digit numbers that start 123, so they are indeed < 2<sup>54</sup>.]</p>

### 입력 

 <p>Input to your program will be multiple lines each containing the number of bulbs, N, the time since they were turned on, t, and the bulb number we are interested in, b, separated by spaces. Read until at end of file, there is no end of data indicator.</p>

### 출력 

 <p>Indicate if the specified bulb is on or off at the end of the requested time. Follow this format exactly: “Case”, a space, the case number, a colon and one space, and the answer which is either “On” or “Off”. Do not print any trailing spaces.</p>

