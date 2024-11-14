# [Gold III] uHunt - 9797 

[문제 링크](https://www.acmicpc.net/problem/9797) 

### 성능 요약

메모리: 46852 KB, 시간: 2120 ms

### 분류

자료 구조, 세그먼트 트리, 트리를 사용한 집합과 맵

### 제출 일자

2024년 11월 14일 14:44:19

### 문제 설명

<p>For those who don't know, uHunt stands for "UVa Hunting", a tool for UVa online-judge that keeps track which problems you have solved and provides statistics as well as a number of selections for the next problem to solve.</p>

<p>This website is created by my brother Felix Halim. Considering that so far, UVa online-judge has about 9 million submissions (approximately one submission per few seconds), about 3000 different programming problems, and about 120000 different users (probably only thousands are currently active), my brother has to highly optimize this tool so that all its features runs "in an instant".</p>

<p>In this problem, we will concentrate on a small subset of uHunt feature, the "instant re-ranking of accepted submissions". One parameter that is ranked in UVa online judge is the accepted submission's runtime speed on judge's data and judge's machine. Suppose we are dealing with problem_id "100". Previously there were 4 accepted submissions for this problem with the following rankings in this format: (rank, user_name, runtime_speed_in_seconds):</p>

<pre>1. josh 0.120
2. nhahtdh 0.127
3. felix 0.223
4. steven 0.323</pre>

<p>Now if user "you" submits an accepted code for problem_id "100" and this code is judged to have a runtime of 0.127s, then "you" will be placed as the new rank 3 with "felix" and "steven" demoted to rank 4 and 5, respectively. Note that although "you" ties with "nhahtdh", "you" will be ranked after "nhahtdh", who submitted his accepted code earlier.</p>

<pre>1. josh 0.120
2. nhahtdh 0.127
<strong>3. you 0.127</strong>
4. felix 0.223
5. steven 0.323</pre>

<p>Suppose user "you" is not happy to get rank 3 and choose to improve his accepted code for problem_id "100". Upon resubmission, his new code (that contains more implementation hack) is judged to have a runtime of 0.115s, then "you" will be placed as the new rank 1 with "josh" and "nhahtdh" demoted to rank 2 and 3, respectively. Notice that "felix" and "steven" stays at rank 4 and 5, respectively.</p>

<pre><strong>1. you 0.115</strong>
2. josh 0.120
3. nhahtdh 0.127
4. felix 0.223
5. steven 0.323</pre>

<p>If another user "grace" submits an accepted code for problem_id "100" with runtime 3.475s, Then the new ranking will be:</p>

<pre>1. you 0.115
2. josh 0.120
3. nhahtdh 0.127
4. felix 0.223
5. steven 0.323
<strong>6. grace 3.475</strong></pre>

<p>Suppose after further tinkering with his program, user "you" submits another accepted code for problem_id "100" with runtime 0.121s.</p>

<p>Since this is actually slower than his previous best, UVa online judge (and uHunt) "ignores" this submission. The ranking stays at:</p>

<pre>1. you 0.115
2. josh 0.120
3. nhahtdh 0.127
4. felix 0.223
5. steven 0.323
6. grace 3.475</pre>

### 입력 

 <p>The first line of input is n (1 ≤ n ≤ 50000), the number of submissions sorted by submission time. You have to process these submissions one after another.</p>

<p>Then, there will be n lines of three numbers: problem_id, user_id, and t. problem_id is a 3 digits integer of problem numbers within range [100-199]. user_id is a 4 digits integer of coder identification id within range [0000-9999]. t is a real number with at most 3 digits after decimal points.</p>

<p>You can be sure that t will not be larger than 9.999 (as the time limit for all problems is < 10 seconds). This t is the runtime of accepted codes of user user_id for problem problem_id.</p>

### 출력 

 <p>For each line of input, immediately output five numbers separated by a single space: problem_id, user_id, and t -- these three are the same as input, then followed by: best_t_for_this_problem_id, and finally: rank_of_user_id_for_this_problem_id</p>

<p>best_t_for_this_problem_id is defined as the runtime of the accepted code submitted by the best coder (who is currently rank 1) for this particular problem.</p>

<p>rank_of_user_id_for_this_problem_id is defined as the ranking of the current coder for this particular problem as described in the problem description above.</p>

<p>However, if that submission from a certain user is actually slower than or equal to his previous best, Then output: "submission ignored" (without the quotes), in one line instead.</p>

