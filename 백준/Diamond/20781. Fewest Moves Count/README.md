# [Diamond II] Fewest Moves Count - 20781 

[문제 링크](https://www.acmicpc.net/problem/20781) 

### 성능 요약

메모리: 1065572 KB, 시간: 41828 ms

### 분류

애드 혹, 너비 우선 탐색, 브루트포스 알고리즘, 그래프 이론, 그래프 탐색, 구현, 수학, 중간에서 만나기, 런타임 전의 전처리

### 제출 일자

2025년 4월 17일 20:49:09

### 문제 설명

<p>Sean is one of the best cubers in China. Today, he is participating in the Fewest Moves Count event of the Chinese Competition of Pocket Cube (CCPC).</p>

<p>A pocket cube is the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>2</mn><mo>×</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \times 2 \times 2$</span></mjx-container> equivalent of the Rubik's cube. Each face of the cube can be rotated, either clockwise or counterclockwise. A standard solved pocket cube has the following color scheme (as shown in Figure 4): the top face is yellow, the bottom face is white, the left face is orange, the right face is red, the front face is blue, the back face is green. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a0eab521-423e-4df6-8cee-45680b3e5d48/-/preview/" style="width: 414px; height: 300px;"></p>

<p style="text-align: center;">Figure 4: The solved state of a standard pocket cube</p>

<p>The Fewest Moves Count event requires a player to find a sequence of moves to transform one configuration of the pocket cube into another, and the player who finds the shortest such sequence among all participants wins the event. In this event, the player can twist any of the six faces in either direction; also, rotating the entire pocket cube is allowed. Note that a quarter twist counts as one move, and a half twist counts as two moves; however, rotating the entire cube doesn't count into the total number of moves.</p>

<p>Since there are millions of essentially different configurations, the task is too hard for Sean and he can't solve it independently. He wants you to write a program to find the minimum number of moves, given the initial and final configurations. Can you help him?</p>

### 입력 

 <p>The first line of input contains a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><mn>250</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq T \leq 250\,000)$</span></mjx-container>, denoting the number of the test cases.</p>

<p>Each test case begins with an empty line followed by six lines, representing the initial and final configurations. A configuration is represented as a net of the pocket cube in the following format:</p>

<pre>  XX    
  XX    
XXXXXXXX
XXXXXXXX
  XX    
  XX    
</pre>

<p>where <code>X</code> is one of the uppercase letters in {<code>G</code>, <code>O</code>, <code>Y</code>, <code>R</code>, <code>W</code>, <code>B</code>}, denoting green, orange, yellow, red, white, and blue, respectively, and all other characters are whitespaces. The initial and final configurations are horizontally stacked together, with each line split by a vertical bar <code>|</code>. In other words, the 1st to the 8th columns represent the initial configuration, the 9th column is vertical bars, and the 10th to the 17th columns represent the final configuration. It is guaranteed that both configurations are legal, that is, they can be recovered to the solved state by a finite sequence of moves.</p>

### 출력 

 <p>For each test case, output a single integer in a line, denoting the minimum number of moves required to transform the initial configuration into the final one.</p>

