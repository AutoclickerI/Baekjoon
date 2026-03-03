# [Unrated] 진짜 최종 구데기컵 1 경품 당첨자 - 21299 

[문제 링크](https://www.acmicpc.net/problem/21299) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

분류 없음

### 제출 일자

2026년 3월 3일 17:07:35

### 문제 설명

<p>구데기컵 주최자 사퇴를 선언한 jh05013은 일처리도 제대로 안 했다! 경품 당첨자 발표 및 지급을 무려 1년이나 미루고 있다.</p>

<p>올해 구데기컵의 경품을 준비하고 있는 ???은 테스트를 위해 작년 구데기컵의 경품 목록을 이리저리 섞고 있었다. 작년의 경품은 진작 지급이 끝났을 것이라고 생각했기 때문이다. 하지만 jh05013은 이왕 이렇게 된 거 올해 경품을 지급할 때 작년 경품을 같이 지급할 계획이었다. 그가 ???의 행보를 알아차리고 급히 경품 목록을 펼쳐 보았을 때에는 이미 모든 것이 뒤죽박죽 섞여 있었다!</p>

<p>jh05013은 급히 원본 목록을 복원해 보겠다고 했지만, ???은 주최자도 출제자도 아닌 주제에 좀 가만히 있으라며 jh05013의 손에 들린 목록을 회수해 갔다.</p>

### 입력 

 <p>경품 당첨 기준이 주어진다. 이는 다음 중 하나이다.</p>

<ul>
	<li>Marathon Edition 우승자</li>
	<li>Marathon Edition 준우승자 및 ReguIar Edition 준우승자</li>
	<li>ReguIar Edition 우승자 및 Speedrun Edition 우승자</li>
	<li>Speedrun Edition 준우승자</li>
	<li>이 대회에 참가하지 않은 사람 중 2019년 대회 최고 등수</li>
	<li>모든 에디션에서 총점이 160억점에 가장 가까운 사람</li>
	<li>홀수와 짝수의 대결 문제의 오류를 발견한 사람</li>
	<li>4차 산업 혁명을 기계학습 없이 서브태스크 2까지만 푼 사람 중 추첨</li>
	<li>배중률교를 정해가 아닌 방법으로 푼 사람 중 추첨</li>
	<li>Marathon Edition에서 Nonogram QR을 마지막으로 1점 이상 획득한 사람</li>
	<li>연속합 2147483647 첫 0점자</li>
	<li>Beginning the Hunt 첫 만점자</li>
	<li>대회에 참여하였고 A+B (MC)에 제출하지 않은 사람 중 추첨</li>
</ul>

### 출력 

 <p>첫째 줄에 상의 이름, 둘째 줄에 경품의 이름, 셋째 줄에 경품 당첨자의 아이디를 출력한다.</p>

<p>상의 이름은 다음 중 하나이다.</p>

<ul>
	<li>대상</li>
	<li>장려상</li>
	<li>QR 분해 상</li>
	<li>"Ghudegy Cup looks too intense for me" 상</li>
	<li>QA 상</li>
	<li>결근상</li>
	<li>Re: 제로부터 시작하는 다이나믹 프로그래밍 상</li>
	<li>You Need a Minecraft 상</li>
	<li>UPWF 위원회 특별상</li>
	<li>직관주의자상</li>
</ul>

<p>경품의 이름은 다음 중 하나이다.</p>

<ul>
	<li>치킨 기프티콘</li>
	<li>빵</li>
	<li>(도서) 4차 산업혁명은 없다</li>
	<li>(도서) Speedrun Science: A Long Guide To Short Playthroughs</li>
	<li>16GB USB</li>
	<li>
	레고 타워 브리지 - 10214</li>
	<li>바코드 스캐너</li>
	<li>Katamari Damacy REROLL</li>
	<li>Minecraft</li>
	<li>Roller Coaster Tycoon 2: Triple Thrill Pack</li>
</ul>

<p>당첨자 아이디는 다음 중 하나이다.</p>

<ul>
	<li>201812106</li>
	<li>rubix</li>
	<li>portableangel</li>
	<li>sait2000</li>
	<li>hyeonguk</li>
	<li>greimul</li>
	<li>dotorya</li>
	<li>2u_my_light</li>
	<li>namnamseo</li>
	<li>cubelover</li>
	<li>pichulia</li>
	<li>xiaowuc1</li>
	<li>zigui</li>
</ul>

<p>모든 데이터를 통틀어서 39개의 줄을 올바르게 출력해야 한다. 올바르게 출력한 줄이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>개일 때, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mrow space="4"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230A TEX-S1"></mjx-c></mjx-mo><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230B TEX-S1"></mjx-c></mjx-mo></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">⌊</mo><mfrac><mi>x</mi><mn>3</mn></mfrac><mo data-mjx-texclass="CLOSE">⌋</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$y = \left\lfloor \frac{x}{3} \right\rfloor$</span></mjx-container>라고 하자. 이때 점수는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230A TEX-S1"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c37"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mfrac space="3"><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230B TEX-S1"></mjx-c></mjx-mo></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">⌊</mo><mn>1000000007</mn><mo>×</mo><mfrac><mi>y</mi><mn>13</mn></mfrac><mo data-mjx-texclass="CLOSE">⌋</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\left\lfloor 1000000007 \times \frac{y}{13} \right\rfloor$</span></mjx-container>이다.</p>

