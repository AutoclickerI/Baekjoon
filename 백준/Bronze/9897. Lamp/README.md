# [Bronze II] Lamp - 9897 

[문제 링크](https://acmicpc.net/problem/9897) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 자료 구조, 문자열, 브루트포스 알고리즘, 시뮬레이션, 집합과 맵, 해시를 사용한 집합과 맵

### 제출 일자

2025년 4월 9일 16:02:56

### 문제 설명

<p>A building has a long corridor and&nbsp;<i>L</i>&nbsp;ceiling lamps labeled 1, 2, 3, ...,&nbsp;<i>L</i>. Each lamp has an individual switch that can turn the lamp on or off. The building manager hires&nbsp;<i>G</i>&nbsp;security guards (no two guards have the same name), whose job at night is to patrol the corridor and turn the lamps on and off. Each guard is assigned a subset of lamps. During one patrol round, a guard will walk along the corridor, and toggle the lamps assigned to him/her (that is, if a lamp is on, switch it off; if the lamp is off, switch it on). After a guard toggles each lamp assigned to him/her exactly once, the guard will take a break until his/her next patrol round. A guard may have more than one patrol round in one night. The order of patrol for the guards is dictated by a duty roster.</p>

<p>All lamps are off before the guards begin their patrol rounds, and there is only one guard on patrol at any time.</p>

<p>The assignment of lamps to a guard is specified by two positive integers,&nbsp;<i>a</i><sub>0</sub>&nbsp;and&nbsp;<i>d</i>. The subset of lamps the guard will toggle is</p>

<p style="text-align: center;">{<i>a</i><sub>0</sub>,&nbsp;<i>a</i><sub>0</sub>&nbsp;+&nbsp;<i>d</i>,&nbsp;<i>a</i><sub>0</sub>&nbsp;+ 2<i>d</i>, ...,&nbsp;<i>a</i><sub>0</sub>&nbsp;+&nbsp;<i>kd</i>}</p>

<p>where&nbsp;<i>k</i>&nbsp;is the largest integer such that&nbsp;<i>a</i><sub>0</sub>&nbsp;+&nbsp;<i>kd</i>&nbsp;≤&nbsp;<i>L</i>.</p>

<p>Given the lamp assignment for each guard and the duty roster, find out how many lamps are on after all the guards have finished all of their patrol rounds.</p>

<p>Suppose we have 10 lamps, two security guards (Edi and Lou), and three patrol rounds. Edi's lamp assignment is (<i>a</i><sub>0</sub>,&nbsp;<i>d</i>) = (1, 4) and Lou's lamp assignment is (<i>a</i><sub>0</sub>,&nbsp;<i>d</i>) = (2, 3). The order of patrol is Edi, Lou, Edi.</p>

<p>After the first patrol round by Edi, lamps 1, 5, and 9 will be on. During the second patrol round, Lou toggles lamps 2, 5, and 8. Therefore, after the second patrol round, lamps 1, 2, 8, and 9 are on but lamp 5 has been turned off. On the third patrol round, Edi patrols again, and toggles lamps 1, 5, and 9. Consequently, after all the patrol rounds specified in the duty roster, the lamps that are on are 2, 5, and 8.</p>

<p>The number of lamps that are still on after the guards finish their patrol rounds is therefore 3.</p>

### 입력 

 <p>The first line in input&nbsp;consists of three positive integers, separated with a blank character. The first number&nbsp;<i>L</i>&nbsp;≤ 1000 is the number of lamps. The second number&nbsp;<i>G</i>&nbsp;≤ 10 is the number of security guards, and the third number&nbsp;<i>R</i>&nbsp;≤ 50 is the total number of patrol rounds. The next&nbsp;<i>G</i>&nbsp;lines contain the names and lamp assignments of the guards. Each of these&nbsp;<i>G</i>&nbsp;lines consists of the name (exactly 3 English letters),&nbsp;<i>a</i><sub>0</sub>&nbsp;and&nbsp;<i>d</i>, (<i>a</i><sub>0</sub>&nbsp;≤&nbsp;<i>N</i>) separated with a blank character. The subsequent&nbsp;<i>R</i>&nbsp;lines specify the duty roster. Each line contains the name of a guard (guaranteed to have lamp assignment). The order of the guards appearing in the duty roster dictates the order of their patrol.</p>

### 출력 

 <p>The output&nbsp;contains one integer which is the number of lamps that are on after all guards finish all of their patrol rounds.</p>

