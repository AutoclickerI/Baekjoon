# [Platinum I] range - 17445 

[문제 링크](https://www.acmicpc.net/problem/17445) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

많은 조건 분기, 수학

### 문제 설명

<p>SNUPC의 지원 언어이기도 한 Python에는 <code>range</code>라는 class가 있습니다. 이 class는 유한 등차수열을 표현하기 위해 만들어졌습니다.</p>

<p>유한 등차수열 {<span style="font-style: italic;">a</span><sub><span style="font-style: italic;">i</span></sub>} = [<span style="font-style: italic;">a</span><sub>0</sub>, …, <span style="font-style: italic;">a</span><sub><span style="font-style: italic;">L</span>-1</sub>]은 세 정수 <span style="font-style: italic;">s</span>, <span style="font-style: italic;">e</span>, <span style="font-style: italic;">d</span>(<span style="font-style: italic;">d</span> ≠ 0)로 특징될 수 있으며, 초항이 <span style="font-style: italic;">s</span>이고 공차가 <span style="font-style: italic;">d</span>인 등차수열 {<span style="font-style: italic;">D</span><sub><span style="font-style: italic;">i</span></sub>} 중 {<span style="font-style: italic;">x </span>: <span style="display: inline-block; position: relative; vertical-align: middle; letter-spacing: 0.001em; text-align: center;"><span style="display: block; padding: 0.1em;">|<span style="font-style: italic;">d</span>|</span><span style="display: none; padding: 0.1em;">/</span><span style="display: block; padding: 0.1em; border-top: thin solid black;"><span style="font-style: italic;">d</span></span></span>·<span style="font-style: italic;">s</span> ≤ <span style="display: inline-block; position: relative; vertical-align: middle; letter-spacing: 0.001em; text-align: center;"><span style="display: block; padding: 0.1em;">|<span style="font-style: italic;">d</span>|</span><span style="display: none; padding: 0.1em;">/</span><span style="display: block; padding: 0.1em; border-top: thin solid black;"><span style="font-style: italic;">d</span></span></span>·<span style="font-style: italic;">x</span> < <span style="display: inline-block; position: relative; vertical-align: middle; letter-spacing: 0.001em; text-align: center;"><span style="display: block; padding: 0.1em;">|<span style="font-style: italic;">d</span>|</span><span style="display: none; padding: 0.1em;">/</span><span style="display: block; padding: 0.1em; border-top: thin solid black;"><span style="font-style: italic;">d</span></span></span>·<span style="font-style: italic;">e</span>}에 속한 원소를 전부 모은 {<span style="font-style: italic;">D</span><sub><span style="font-style: italic;">i</span></sub>}의 유한 부분수열입니다. 예를 들어 <span style="font-style: italic;">s</span> = 0, <span style="font-style: italic;">e</span> = 5, <span style="font-style: italic;">d</span> = 1이 나타내는 유한 등차수열은 [0, 1, 2, 3, 4]입니다.</p>

<p>유한 등차수열의 길이는 그 수열에 속한 수의 집합의 크기입니다. 예를 들어 위 예에서 길이는 5가 됩니다. 두 유한 등차수열 {<span style="font-style: italic;">a</span><sub><span style="font-style: italic;">i</span></sub>}와 {<span style="font-style: italic;">b</span><sub><span style="font-style: italic;">i</span></sub>}가 같다는 것은 두 수열의 길이가 <span style="font-style: italic;">L</span>로 같고, 모든 정수 0 ≤ <span style="font-style: italic;">i</span> < <span style="font-style: italic;">L</span>에 대해 <span style="font-style: italic;">a</span><sub><span style="font-style: italic;">i</span></sub> = <span style="font-style: italic;">b</span><sub><span style="font-style: italic;">i</span></sub>인 경우를 얘기합니다.</p>

<p><code>range</code>는 다음과 같은 세 가지 문법을 지원합니다.</p>

<ul>
	<li><code>range(a)</code>. 이는 <span style="font-style: italic;">s</span> = 0, <span style="font-style: italic;">e</span> = <code>a</code>, <span style="font-style: italic;">d</span> = 1인 유한 등차수열을 나타냅니다.</li>
	<li><code>range(a,b)</code>. 이는 <span style="font-style: italic;">s</span> = <code>a</code>, <span style="font-style: italic;">e</span> = <code>b</code>, <span style="font-style: italic;">d</span> = 1인 유한 등차수열을 나타냅니다.</li>
	<li><code>range(a,b,c)</code>. 이는 <span style="font-style: italic;">s</span> = <code>a</code>, <span style="font-style: italic;">e</span> = <code>b</code>, <span style="font-style: italic;">d</span> = <code>c</code>인 유한 등차수열을 나타냅니다. 이때 <code>c</code>는 0이 아니어야 합니다.</li>
</ul>

<p>Python에서는 놀랍게도 <code>range</code>끼리 같은지 비교할 때, <code>range</code>가 나타내는 수열 표현으로 비교합니다. 예를 들어 <code>range(5)</code>와 <code>range(0,5)</code>는 수열 표현이 [0, 1, 2, 3, 4]로 같으므로 같다고 판단합니다. 또한 수열의 길이는 0이 될 수 있습니다. 예를 들어 <code>range(5,9,-3)</code>과 <code>range(7,2)</code>는 모두 수열의 길이가 0이므로 같다고 판단합니다.</p>

<p>당신의 일은 Python의 <code>range</code>를 하나 받아서 그와 같다고 판단되는 <code>range</code>를 출력하는 것입니다.</p>

### 입력 

 <p>첫 줄에 <code>range</code>가 주어집니다. 문자열의 각 문자는 <code>(),-0123456789aegnr</code> 중 하나입니다. 지문에 있는 괄호 속의 <code>a</code>, <code>b</code>, <code>c</code>는 절댓값이 10<sup>9</sup>보다 작은 정수로 대체되어 주어집니다.</p>

<p>이때 정수 <span style="font-style: italic;">n</span>을 표현하는 문자열은,</p>

<ul>
	<li><span style="font-style: italic;">n</span>>0인 경우 십진법 숫자로만 구성되며, 첫 문자는 <code>0</code>이 아닙니다. <span style="font-style: italic;">n</span>은 이 문자열의 십진 전개를 계산한 값입니다.</li>
	<li><span style="font-style: italic;">n</span>=0인 경우 항상 <code>0</code>입니다.</li>
	<li><span style="font-style: italic;">n</span><0인 경우 첫 문자는 <code>-</code>이며, 첫 문자를 제외한 문자열은 (-<span style="font-style: italic;">n</span>)을 표현하는 문자열입니다.</li>
</ul>

<p><code>range</code>의 인자의 개수는 하나, 둘 또는 셋 모두 들어올 수 있습니다.</p>

### 출력 

 <p>첫 줄에 Python이 입력과 같다고 판단하는 <code>range</code>를 나타내는 문자열을 출력합니다. 정수의 표현은 입력 조건과 같아야 하며, 각 수의 절댓값이 반드시 10<sup>9</sup>보다 작을 필요는 없습니다.</p>

<p>가능한 문자열이 여럿 있으면 <strong>사전 순으로 최소인 문자열</strong>을 출력합니다. 이때, 각 문자는 미국 정보 교환 표준 부호(ASCII) 순서, 즉 <code>(),-0123456789aegnr</code>(앞에 있을수록 작음) 순서로 비교합니다.</p>

