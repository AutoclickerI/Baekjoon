# [Gold I] Tiny - 2 - 22202 

[문제 링크](https://www.acmicpc.net/problem/22202) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

애드 혹, 해 구성하기, 휴리스틱, 구현, 시뮬레이션, 문자열

### 문제 설명

<p>Elder people still remember the famous computer game “TETRIS” created by Alexey Pajitnov, where pieces consisting of four squares (tetrominoes) fall from the sky and the goal of the game is to rotate and land every piece in a rectangular container creating as many lines of blocks without gaps as possible. When such lines are created, they disappear giving more space for the following pieces.</p>

<p>Let’s investigate a simpler version of the game, called “Tiny TETRIS” (or just “Tiny” for short). There are only nine different Tiny pieces (or t-pieces) consisting of one to three squares:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 492px; height: 97px;"></p>

<p>The number denotes the type of a t-piece and will be used further to reference the particular t-piece.</p>

<p>The goal of the game is the same – falling t-pieces must be put in a rectangular container which is 9 units wide and 9 units high. Contrary to TETRIS, t-pieces cannot be rotated. Moreover, they cannot be moved to the left or right after they start falling. Thus, for each t-piece the player must only choose the container’s column number (integer from 1 to 9) where the leftmost square of the piece (marked as × ) will fall.</p>

<p>Each game consists of a finite sequence of N t-pieces from which as many as possible must be dropped in the container without exceeding its upper level or making an illegal move. The score of the game is equal to the number of successfully dropped t-pieces.</p>

<p>At the beginning the game counter is set to 0.</p>

<p>The algorithm of the game is the following:</p>

<ol>
	<li>Player chooses the column for the leftmost square of the current t-piece;</li>
	<li>If the column is set correctly (for example, column 8 can never be correct for the t-piece 5), t-piece falls down until it meets an obstacle; otherwise the game is over.</li>
	<li>If the t-piece fully fits inside the container (i.e., all squares are inside the 9×9 rectangle) the value of the counter is increased by one. Otherwise, the game is over.</li>
	<li>Then it is checked whether there are any completed horizontal lines (horizontal lines filled completely with blocks of t-pieces without any gaps). If there are any then these lines disappear and the lines above them are shifted down without changing their configuration.</li>
	<li>If there are any t-pieces left, proceed to 1). Otherwise the game is over.</li>
</ol>

<p>Score of a particular game is the value of the counter at the moment when the game ends.</p>

<p>Let’s analyze one particular game.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 191px; height: 195px;"></p>

<p>Sequence of the given 20 t-pieces is the following: 5,4,1,6,7,6,4,4,7,9,5,5,6,8,3,4,3,7,4,2. Let’s assume that the first 17 t-pieces have already been successfully dropped in the container in the columns 1,2,2,4,8,8,7,4,8,6,1,1,4,8,3,7,7, respectively. Until this moment no lines have been completed, the current value of the counter is 17 and it is time to drop t-piece 7 (letters in the figure are assigned consecutively to t-pieces):</p>

<p>There are only two valid columns where t-piece 7 can be dropped:</p>

<table class="table table-bordered td-center" style="width:100%;">
	<thead>
		<tr>
			<th style="width:50%;">a) column 1:</th>
			<th style="width:50%;">b) column 5 (in this case one line will be completed and, therefore, disappear):</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><img alt="" src="" style="width: 225px; height: 231px;"></td>
			<td><img alt="" src="" style="width: 225px; height: 231px;"></td>
		</tr>
	</tbody>
</table>

<p>You are given five files each containing a description of a particular game: <a href="https://upload.acmicpc.net/3ce8d27a-89df-44e5-8c7a-a4777b43cabc/">tiny.i01</a>, <a href="https://upload.acmicpc.net/f16e51ff-adef-4bc7-9e87-238f620d4dbd/">tiny.i02</a>, <a href="https://upload.acmicpc.net/0401e1e1-0592-4f7f-b44f-f8b7e96b3317/">tiny.i03</a>, <a href="https://upload.acmicpc.net/62ba0009-568c-4069-904b-de3809eff350/">tiny.i04</a> and <a href="https://upload.acmicpc.net/acea5a0f-9749-4746-ae0d-574785d49ae7/">tiny.i05</a>. Each file contains the sequence of t-pieces and has the following format: the first line contains a single integer N. The next N lines describe the t-piece sequence; each line contains an integer between 1 and 9 – the number of the particular t-piece. T-pieces are given in the order how they must be dropped in the container; the i-th t-piece is given in the i+1-st line of the file.</p>

<p>For each of the given input file you must submit a corresponding output file with at most N rows – the numbers of the columns where pieces are dropped. The i-th row of the output file must contain the number of the column where the i-th t-piece from the input data must be dropped.</p>

<p>It is guaranteed that for each input file there exists a sequence of columns which allows all t-pieces to be successfully dropped in the container (and gets the final score for the game equal to N).</p>

### 입력 

 Empty

### 출력 

 Empty

