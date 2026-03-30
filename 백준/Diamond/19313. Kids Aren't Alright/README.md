# [Diamond V] Kids Aren't Alright - 19313 

[문제 링크](https://www.acmicpc.net/problem/19313) 

### 성능 요약

메모리: 210160 KB, 시간: 5664 ms

### 분류

수학, 정수론, 소인수분해, 폴라드 로

### 제출 일자

2026년 3월 30일 09:07:04

### 문제 설명

<p>As unlikely as it may seem, a crazy guy on the phone claims to have kidnapped your precious child. You don't really believe him, as all your children (possibly none) are playing in front of you right now, safe and sound. Anyway, you're fairly curious about the situation, so you ask the criminal what he wants for releasing his hostage.</p>

<p>As boring as it may seem, the kidnapper asks for money. Just money. You are about to hang up the phone in disappointment when something peculiar attracts your attention. Your interlocutor is not telling you the exact amount he wants. Instead, he proposes you a riddle.</p>

<p>As ridiculous as it may seem, the riddle is:</p>

<p>"<em>How many non-empty sets of positive integers exist such that their greatest common divisor is 1, while their least common multiple is <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container>?</em>".</p>

<p>Then, the abductor tells you that the answer to this riddle, taken modulo <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>998244353</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$998244353$</span></mjx-container>, is the exact amount of money he wants for returning your imaginary offspring.</p>

<p>You're now wondering about the rates at the kidnapping market, since you've been away from this kind of affairs for quite some time. Not that you're going to pay the snatcher a single penny, though.</p>

### 입력 

 <p>The only line of the input contains a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>m</mi><mo>≤</mo><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mn>18</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le m \le 10^{18}$</span></mjx-container>).</p>

### 출력 

 <p>Output a single integer --- the amount of money you've been asked for.</p>

