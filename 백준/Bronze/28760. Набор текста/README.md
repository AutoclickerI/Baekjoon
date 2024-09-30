# [Bronze I] Набор текста - 28760 

[문제 링크](https://www.acmicpc.net/problem/28760) 

### 성능 요약

메모리: 31252 KB, 시간: 32 ms

### 분류

문자열

### 제출 일자

2024년 9월 30일 17:58:31

### 문제 설명

<p>Роман Сайонис пишет письмо с угрозами для Харли Квин. Он использует простой текстовый редактор и обычную QWERTY-клавиатуру.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/11148633-8ee1-449a-80de-8ed4a6bc1a4f/-/preview/" style="width: 600px; height: 200px;"></p>

<p>В тексте Роман использует строчные и заглавные буквы английского алфавита, цифры, символы <<,>>, <<.>>, <<!>>, <<?>>, <<<span>$</span>>>, <<(>> и <<)>>, а также пробелы. Текстовый редактор Сайониса настолько прост, что позволяет только дописывать в конец текущего сообщения по одному символу, нажимая на соответствующие клавиши на клавиатуре. Даже если Сайонис хочет набрать несколько одинаковых символов подряд, ему придется нажимать на клавишу заново для каждого символа. Помимо клавиш, соответствующих набираемым символам, Роман использует только клавишу shift, когда это необходимо для набора очередного символа. Среди используемых им символов, shift должен быть нажат, чтобы набрать заглавные буквы и символы <<!>>, <<?>>, <<<span>$</span>>>, <<(>> и <<)>>. Пробел может быть набран как с нажатой клавишей shift, так и без неё. А во время набирания всех остальных символов, клавиша shift должна быть не нажата.</p>

<p>Роман очень спешит, поэтому хочет набрать сообщение, нажав на клавиши минимальное количество раз. Для экономии времени, он может нажать клавишу shift, набрать несколько символов, и только затем отпустить её --- это будет считаться одним нажатием клавиши shift. Помогите Роману определить минимальное количество нажатий на клавиши, которое ему придется сделать.</p>

### 입력 

 <p>В первой строке дано одно целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- число символов в тексте Романа (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 10\,000$</span></mjx-container>).</p>

<p>Во второй строке дана строка длины <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>, состоящая из строчных и заглавных букв английского алфавита, цифр, символов <<,>>, <<.>>, <<!>>, <<?>>, <<<span>$</span>>>, <<(>>, <<)>> и пробелов.</p>

### 출력 

 <p>Выведите одно число --- минимальное количество нажатий на клавиши, которое придется сделать Роману.</p>

