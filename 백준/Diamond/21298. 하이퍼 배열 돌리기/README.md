# [Diamond V] 하이퍼 배열 돌리기 - 21298 

[문제 링크](https://www.acmicpc.net/problem/21298) 

### 성능 요약

메모리: 225548 KB, 시간: 5092 ms

### 분류

구현, 기하학, 4차원 이상의 기하학

### 제출 일자

2026년 3월 13일 16:20:46

### 문제 설명

<p>$m$축, $n$축, $o$축, $p$축, $q$축, $r$축, $s$축, $t$축, $u$축, $v$축, $w$축에 대해 모양이 $M \times N \times O \times P \times Q \times R \times S \times T \times U \times V \times W$인 <span class="__h_hyper">하이퍼 배열</span> <span class="__h_hyper">$A$</span>가 있을 때, <span class="__h_hyper">하이퍼 배열</span>에 연산을 $\rho$개 적용하려고 한다. 연산은 총 $121$가지가 있다.</p>

<ul>
	<li>$1$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $nopqrstuvw$-초공간에 대해 대칭한다.</li>
	<li>$2$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mopqrstuvw$-초공간에 대해 대칭한다.</li>
	<li>$3$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnpqrstuvw$-초공간에 대해 대칭한다.</li>
	<li>$4$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnoqrstuvw$-초공간에 대해 대칭한다.</li>
	<li>$5$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnoprstuvw$-초공간에 대해 대칭한다.</li>
	<li>$6$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnopqstuvw$-초공간에 대해 대칭한다.</li>
	<li>$7$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnopqrtuvw$-초공간에 대해 대칭한다.</li>
	<li>$8$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnopqrsuvw$-초공간에 대해 대칭한다.</li>
	<li>$9$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnopqrstvw$-초공간에 대해 대칭한다.</li>
	<li>$10$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnopqrstuw$-초공간에 대해 대칭한다.</li>
	<li>$11$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$을 $mnopqrstuv$-초공간에 대해 대칭한다.</li>
	<li>$12$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+n$이 아래 방향인 $mn$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$13$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+o$가 아래 방향인 $mo$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$14$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+p$가 아래 방향인 $mp$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$15$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+q$가 아래 방향인 $mq$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$16$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+r$가 아래 방향인 $mr$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$17$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+s$가 아래 방향인 $ms$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$18$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+t$가 아래 방향인 $mt$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$19$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+u$가 아래 방향인 $mu$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$20$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+v$가 아래 방향인 $mv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$21$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+m$이 오른쪽 방향이고 $+w$가 아래 방향인 $mw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$22$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+o$가 아래 방향인 $no$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$23$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+p$가 아래 방향인 $np$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$24$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+q$가 아래 방향인 $nq$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$25$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+r$가 아래 방향인 $nr$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$26$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+s$가 아래 방향인 $ns$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$27$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+t$가 아래 방향인 $nt$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$28$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+u$가 아래 방향인 $nu$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$29$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+v$가 아래 방향인 $nv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$30$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+n$이 오른쪽 방향이고 $+w$가 아래 방향인 $nw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$31$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+p$가 아래 방향인 $op$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$32$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+q$가 아래 방향인 $oq$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$33$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+r$가 아래 방향인 $or$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$34$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+s$가 아래 방향인 $os$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$35$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+t$가 아래 방향인 $ot$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$36$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+u$가 아래 방향인 $ou$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$37$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+v$가 아래 방향인 $ov$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$38$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+o$가 오른쪽 방향이고 $+w$가 아래 방향인 $ow$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$39$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+p$가 오른쪽 방향이고 $+q$가 아래 방향인 $pq$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$40$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+p$가 오른쪽 방향이고 $+r$가 아래 방향인 $pr$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$41$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+p$가 오른쪽 방향이고 $+s$가 아래 방향인 $ps$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$42$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+p$가 오른쪽 방향이고 $+t$가 아래 방향인 $pt$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$43$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+p$가 오른쪽 방향이고 $+u$가 아래 방향인 $pu$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$44$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+p$가 오른쪽 방향이고 $+v$가 아래 방향인 $pv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$45$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+p$가 오른쪽 방향이고 $+w$가 아래 방향인 $pw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$46$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+q$가 오른쪽 방향이고 $+r$가 아래 방향인 $qr$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$47$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+q$가 오른쪽 방향이고 $+s$가 아래 방향인 $qs$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$48$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+q$가 오른쪽 방향이고 $+t$가 아래 방향인 $qt$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$49$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+q$가 오른쪽 방향이고 $+u$가 아래 방향인 $qu$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$50$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+q$가 오른쪽 방향이고 $+v$가 아래 방향인 $qv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$51$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+q$가 오른쪽 방향이고 $+w$가 아래 방향인 $qw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$52$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+r$가 오른쪽 방향이고 $+s$가 아래 방향인 $rs$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$53$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+r$가 오른쪽 방향이고 $+t$가 아래 방향인 $rt$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$54$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+r$가 오른쪽 방향이고 $+u$가 아래 방향인 $ru$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$55$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+r$가 오른쪽 방향이고 $+v$가 아래 방향인 $rv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$56$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+r$가 오른쪽 방향이고 $+w$가 아래 방향인 $rw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$57$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+s$가 오른쪽 방향이고 $+t$가 아래 방향인 $st$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$58$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+s$가 오른쪽 방향이고 $+u$가 아래 방향인 $su$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$59$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+s$가 오른쪽 방향이고 $+v$가 아래 방향인 $sv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$60$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+s$가 오른쪽 방향이고 $+w$가 아래 방향인 $sw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$61$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+t$가 오른쪽 방향이고 $+u$가 아래 방향인 $tu$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$62$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+t$가 오른쪽 방향이고 $+v$가 아래 방향인 $tv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$63$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+t$가 오른쪽 방향이고 $+w$가 아래 방향인 $tw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$64$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+u$가 오른쪽 방향이고 $+v$가 아래 방향인 $uv$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$65$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+u$가 오른쪽 방향이고 $+w$가 아래 방향인 $uw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$66$번 연산은 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$의 모든 원소를 $+v$가 오른쪽 방향이고 $+w$가 아래 방향인 $vw$-평면을 기준으로 반시계방향으로 한 칸씩 이동시킨다.</li>
	<li>$67$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=n$에 대해 대칭한다.</li>
	<li>$68$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=o$에 대해 대칭한다.</li>
	<li>$69$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=p$에 대해 대칭한다.</li>
	<li>$70$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=q$에 대해 대칭한다.</li>
	<li>$71$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=r$에 대해 대칭한다.</li>
	<li>$72$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=s$에 대해 대칭한다.</li>
	<li>$73$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=t$에 대해 대칭한다.</li>
	<li>$74$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=u$에 대해 대칭한다.</li>
	<li>$75$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=v$에 대해 대칭한다.</li>
	<li>$76$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $m=w$에 대해 대칭한다.</li>
	<li>$77$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=o$에 대해 대칭한다.</li>
	<li>$78$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=p$에 대해 대칭한다.</li>
	<li>$79$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=q$에 대해 대칭한다.</li>
	<li>$80$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=r$에 대해 대칭한다.</li>
	<li>$81$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=s$에 대해 대칭한다.</li>
	<li>$82$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=t$에 대해 대칭한다.</li>
	<li>$83$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=u$에 대해 대칭한다.</li>
	<li>$84$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=v$에 대해 대칭한다.</li>
	<li>$85$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $n=w$에 대해 대칭한다.</li>
	<li>$86$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=p$에 대해 대칭한다.</li>
	<li>$87$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=q$에 대해 대칭한다.</li>
	<li>$88$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=r$에 대해 대칭한다.</li>
	<li>$89$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=s$에 대해 대칭한다.</li>
	<li>$90$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=t$에 대해 대칭한다.</li>
	<li>$91$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=u$에 대해 대칭한다.</li>
	<li>$92$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=v$에 대해 대칭한다.</li>
	<li>$93$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $o=w$에 대해 대칭한다.</li>
	<li>$94$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $p=q$에 대해 대칭한다.</li>
	<li>$95$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $p=r$에 대해 대칭한다.</li>
	<li>$96$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $p=s$에 대해 대칭한다.</li>
	<li>$97$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $p=t$에 대해 대칭한다.</li>
	<li>$98$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $p=u$에 대해 대칭한다.</li>
	<li>$99$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $p=v$에 대해 대칭한다.</li>
	<li>$100$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $p=w$에 대해 대칭한다.</li>
	<li>$101$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $q=r$에 대해 대칭한다.</li>
	<li>$102$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $q=s$에 대해 대칭한다.</li>
	<li>$103$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $q=t$에 대해 대칭한다.</li>
	<li>$104$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $q=u$에 대해 대칭한다.</li>
	<li>$105$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $q=v$에 대해 대칭한다.</li>
	<li>$106$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $q=w$에 대해 대칭한다.</li>
	<li>$107$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $r=s$에 대해 대칭한다.</li>
	<li>$108$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $r=t$에 대해 대칭한다.</li>
	<li>$109$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $r=u$에 대해 대칭한다.</li>
	<li>$110$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $r=v$에 대해 대칭한다.</li>
	<li>$111$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $r=w$에 대해 대칭한다.</li>
	<li>$112$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $s=t$에 대해 대칭한다.</li>
	<li>$113$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $s=u$에 대해 대칭한다.</li>
	<li>$114$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $s=v$에 대해 대칭한다.</li>
	<li>$115$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $s=w$에 대해 대칭한다.</li>
	<li>$116$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $t=u$에 대해 대칭한다.</li>
	<li>$117$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $t=v$에 대해 대칭한다.</li>
	<li>$118$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $t=w$에 대해 대칭한다.</li>
	<li>$119$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $u=v$에 대해 대칭한다.</li>
	<li>$120$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $u=w$에 대해 대칭한다.</li>
	<li>$121$번 연산은 전체 <span class="__h_hyper">하이퍼 배열</span>을 초공간 $v=w$에 대해 대칭한다.</li>
</ul>

<p><span class="__h_hyper">하이퍼 배열</span>과 $\rho$개의 연산이 주어졌을 때, <span class="__h_hyper">하이퍼 배열</span>에 연산들을 적용한 결과를 구해보자.</p>

### 입력 

 <p>첫째 줄의 <span class="__h_hyper">하이퍼 배열</span>의 모양 $M$, $N$, $O$, $P$, $Q$, $R$, $S$, $T$, $U$, $V$, $W$가 주어진다. ($1 \le M,N,O,P,Q,R,S,T,U,V,W,MNOPQRSTUVW \le 111\,111$)</p>

<p>둘째 줄부터는 배열 <span class="__h_hyper">$A$</span>의 원소들이 아래와 같이 주어진다. ($1 \le\,$<span class="__h_hyper">$A$</span>$_{mnopqrstuvw} \le 11\,111\,111\,111$)</p>

<ul>
	<li>둘째 줄에는 <span class="__h_hyper">$A$</span>$_{11111111111}$, <span class="__h_hyper">$A$</span>$_{11111111112}$, ..., <span class="__h_hyper">$A$</span>$_{1111111111W}$의 수 $W$개가 주어진다.</li>
	<li>이러한 줄이 $V$번 반복되어 <span class="__h_hyper">$A$</span>$_{11111111111}$, <span class="__h_hyper">$A$</span>$_{11111111112}$, ..., <span class="__h_hyper">$A$</span>$_{111111111VW}$의 수 $VW$개가 주어진다.</li>
	<li>이러한 $V$개의 줄이 $U$번 반복되어 <span class="__h_hyper">$A$</span>$_{11111111111}$, <span class="__h_hyper">$A$</span>$_{11111111112}$, ..., <span class="__h_hyper">$A$</span>$_{11111111UVW}$의 수 $UVW$개가 주어진다.</li>
	<li>이러한 $UV$개의 줄이 $T$번 반복되어 <span class="__h_hyper">$A$</span>$_{11111111111}$, <span class="__h_hyper">$A$</span>$_{11111111112}$, ..., <span class="__h_hyper">$A$</span>$_{1111111TUVW}$의 수 $TUVW$개가 주어진다.</li>
	<li>⋯ 이와 같은 방법으로 $MNOPQRSTUV$개의 줄에 걸쳐 <span class="__h_hyper">$A$</span>$_{11111111111}$, <span class="__h_hyper">$A$</span>$_{11111111112}$, ..., <span class="__h_hyper">$A$</span>$_{MNOPQRSTUVW}$가 주어진다.</li>
</ul>

<p>다음 줄에는 연산의 수 $\rho$가 주어진다. ($1 \le \rho \le 111\,111$)</p>

<p>다음 줄부터 $\rho$개의 줄에 걸쳐 연산에 대한 정보가 주어진다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>op m<sub>1</sub> n<sub>1</sub> o<sub>1</sub> p<sub>1</sub> q<sub>1</sub> r<sub>1</sub> s<sub>1</sub> t<sub>1</sub> u<sub>1</sub> v<sub>1</sub> w<sub>1</sub> m<sub>2</sub> n<sub>2</sub> o<sub>2</sub> p<sub>2</sub> q<sub>2</sub> r<sub>2</sub> s<sub>2</sub> t<sub>2</sub> u<sub>2</sub> v<sub>2 </sub>w<sub>2</sub></code></span><br>
	: 부분 <span class="__h_hyper">하이퍼 배열</span> $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$에 대해 연산 $op$를 수행한다. ($1 \le op \le 66$, $m_1\le m_2$, $n_1\le n_2$, $o_1\le o_2$, $p_1\le p_2$, $q_1\le q_2$, $r_1\le r_2$, $s_1\le s_2$, $t_1\le t_2$, $u_1\le u_2$, $v_1\le v_2$, $w_1\le w_2$)

	<ul>
		<li>$op = 12$인 경우, $m_1 < m_2$이고 $n_1 < n_2$이다. $\min \left\{ m_2-m_1, n_2-n_1 \right\}$은 홀수이다.</li>
		<li>$op = 13$인 경우, $m_1 < m_2$이고 $o_1 < o_2$이다. $\min \left\{ m_2-m_1, o_2-o_1 \right\}$은 홀수이다.</li>
		<li>$op = 14$인 경우, $m_1 < m_2$이고 $p_1 < p_2$이다. $\min \left\{ m_2-m_1, p_2-p_1 \right\}$은 홀수이다.</li>
		<li>$op = 15$인 경우, $m_1 < m_2$이고 $q_1 < q_2$이다. $\min \left\{ m_2-m_1, q_2-q_1 \right\}$은 홀수이다.</li>
		<li>$op = 16$인 경우, $m_1 < m_2$이고 $r_1 < r_2$이다. $\min \left\{ m_2-m_1, r_2-r_1 \right\}$은 홀수이다.</li>
		<li>$op = 17$인 경우, $m_1 < m_2$이고 $s_1 < s_2$이다. $\min \left\{ m_2-m_1, s_2-s_1 \right\}$은 홀수이다.</li>
		<li>$op = 18$인 경우, $m_1 < m_2$이고 $t_1 < t_2$이다. $\min \left\{ m_2-m_1, t_2-t_1 \right\}$은 홀수이다.</li>
		<li>$op = 19$인 경우, $m_1 < m_2$이고 $u_1 < u_2$이다. $\min \left\{ m_2-m_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 20$인 경우, $m_1 < m_2$이고 $v_1 < v_2$이다. $\min \left\{ m_2-m_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 21$인 경우, $m_1 < m_2$이고 $w_1 < w_2$이다. $\min \left\{ m_2-m_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 22$인 경우, $n_1 < n_2$이고 $o_1 < o_2$이다. $\min \left\{ n_2-n_1, o_2-o_1 \right\}$은 홀수이다.</li>
		<li>$op = 23$인 경우, $n_1 < n_2$이고 $p_1 < p_2$이다. $\min \left\{ n_2-n_1, p_2-p_1 \right\}$은 홀수이다.</li>
		<li>$op = 24$인 경우, $n_1 < n_2$이고 $q_1 < q_2$이다. $\min \left\{ n_2-n_1, q_2-q_1 \right\}$은 홀수이다.</li>
		<li>$op = 25$인 경우, $n_1 < n_2$이고 $r_1 < r_2$이다. $\min \left\{ n_2-n_1, r_2-r_1 \right\}$은 홀수이다.</li>
		<li>$op = 26$인 경우, $n_1 < n_2$이고 $s_1 < s_2$이다. $\min \left\{ n_2-n_1, s_2-s_1 \right\}$은 홀수이다.</li>
		<li>$op = 27$인 경우, $n_1 < n_2$이고 $t_1 < t_2$이다. $\min \left\{ n_2-n_1, t_2-t_1 \right\}$은 홀수이다.</li>
		<li>$op = 28$인 경우, $n_1 < n_2$이고 $u_1 < u_2$이다. $\min \left\{ n_2-n_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 29$인 경우, $n_1 < n_2$이고 $v_1 < v_2$이다. $\min \left\{ n_2-n_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 30$인 경우, $n_1 < n_2$이고 $w_1 < w_2$이다. $\min \left\{ n_2-n_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 31$인 경우, $o_1 < o_2$이고 $p_1 < p_2$이다. $\min \left\{ o_2-o_1, p_2-p_1 \right\}$은 홀수이다.</li>
		<li>$op = 32$인 경우, $o_1 < o_2$이고 $q_1 < q_2$이다. $\min \left\{ o_2-o_1, q_2-q_1 \right\}$은 홀수이다.</li>
		<li>$op = 33$인 경우, $o_1 < o_2$이고 $r_1 < r_2$이다. $\min \left\{ o_2-o_1, r_2-r_1 \right\}$은 홀수이다.</li>
		<li>$op = 34$인 경우, $o_1 < o_2$이고 $s_1 < s_2$이다. $\min \left\{ o_2-o_1, s_2-s_1 \right\}$은 홀수이다.</li>
		<li>$op = 35$인 경우, $o_1 < o_2$이고 $t_1 < t_2$이다. $\min \left\{ o_2-o_1, t_2-t_1 \right\}$은 홀수이다.</li>
		<li>$op = 36$인 경우, $o_1 < o_2$이고 $u_1 < u_2$이다. $\min \left\{ o_2-o_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 37$인 경우, $o_1 < o_2$이고 $v_1 < v_2$이다. $\min \left\{ o_2-o_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 38$인 경우, $o_1 < o_2$이고 $w_1 < w_2$이다. $\min \left\{ o_2-o_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 39$인 경우, $p_1 < p_2$이고 $q_1 < q_2$이다. $\min \left\{ p_2-p_1, q_2-q_1 \right\}$은 홀수이다.</li>
		<li>$op = 40$인 경우, $p_1 < p_2$이고 $r_1 < r_2$이다. $\min \left\{ p_2-p_1, r_2-r_1 \right\}$은 홀수이다.</li>
		<li>$op = 41$인 경우, $p_1 < p_2$이고 $s_1 < s_2$이다. $\min \left\{ p_2-p_1, s_2-s_1 \right\}$은 홀수이다.</li>
		<li>$op = 42$인 경우, $p_1 < p_2$이고 $t_1 < t_2$이다. $\min \left\{ p_2-p_1, t_2-t_1 \right\}$은 홀수이다.</li>
		<li>$op = 43$인 경우, $p_1 < p_2$이고 $u_1 < u_2$이다. $\min \left\{ p_2-p_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 44$인 경우, $p_1 < p_2$이고 $v_1 < v_2$이다. $\min \left\{ p_2-p_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 45$인 경우, $p_1 < p_2$이고 $w_1 < w_2$이다. $\min \left\{ p_2-p_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 46$인 경우, $q_1 < q_2$이고 $r_1 < r_2$이다. $\min \left\{ q_2-q_1, r_2-r_1 \right\}$은 홀수이다.</li>
		<li>$op = 47$인 경우, $q_1 < q_2$이고 $s_1 < s_2$이다. $\min \left\{ q_2-q_1, s_2-s_1 \right\}$은 홀수이다.</li>
		<li>$op = 48$인 경우, $q_1 < q_2$이고 $t_1 < t_2$이다. $\min \left\{ q_2-q_1, t_2-t_1 \right\}$은 홀수이다.</li>
		<li>$op = 49$인 경우, $q_1 < q_2$이고 $u_1 < u_2$이다. $\min \left\{ q_2-q_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 50$인 경우, $q_1 < q_2$이고 $v_1 < v_2$이다. $\min \left\{ q_2-q_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 51$인 경우, $q_1 < q_2$이고 $w_1 < w_2$이다. $\min \left\{ q_2-q_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 52$인 경우, $r_1 < r_2$이고 $s_1 < s_2$이다. $\min \left\{ r_2-r_1, s_2-s_1 \right\}$은 홀수이다.</li>
		<li>$op = 53$인 경우, $r_1 < r_2$이고 $t_1 < t_2$이다. $\min \left\{ r_2-r_1, t_2-t_1 \right\}$은 홀수이다.</li>
		<li>$op = 54$인 경우, $r_1 < r_2$이고 $u_1 < u_2$이다. $\min \left\{ r_2-r_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 55$인 경우, $r_1 < r_2$이고 $v_1 < v_2$이다. $\min \left\{ r_2-r_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 56$인 경우, $r_1 < r_2$이고 $w_1 < w_2$이다. $\min \left\{ r_2-r_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 57$인 경우, $s_1 < s_2$이고 $t_1 < t_2$이다. $\min \left\{ s_2-s_1, t_2-t_1 \right\}$은 홀수이다.</li>
		<li>$op = 58$인 경우, $s_1 < s_2$이고 $u_1 < u_2$이다. $\min \left\{ s_2-s_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 59$인 경우, $s_1 < s_2$이고 $v_1 < v_2$이다. $\min \left\{ s_2-s_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 60$인 경우, $s_1 < s_2$이고 $w_1 < w_2$이다. $\min \left\{ s_2-s_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 61$인 경우, $t_1 < t_2$이고 $u_1 < u_2$이다. $\min \left\{ t_2-t_1, u_2-u_1 \right\}$은 홀수이다.</li>
		<li>$op = 62$인 경우, $t_1 < t_2$이고 $v_1 < v_2$이다. $\min \left\{ t_2-t_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 63$인 경우, $t_1 < t_2$이고 $w_1 < w_2$이다. $\min \left\{ t_2-t_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 64$인 경우, $u_1 < u_2$이고 $v_1 < v_2$이다. $\min \left\{ u_2-u_1, v_2-v_1 \right\}$은 홀수이다.</li>
		<li>$op = 65$인 경우, $u_1 < u_2$이고 $w_1 < w_2$이다. $\min \left\{ u_2-u_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>$op = 66$인 경우, $v_1 < v_2$이고 $w_1 < w_2$이다. $\min \left\{ v_2-v_1, w_2-w_1 \right\}$은 홀수이다.</li>
		<li>입력으로 주어지는 모든 수는 정수이고, 연산을 수행하는 시점에서 $\left[m_1,n_1,o_1,p_1,q_1,r_1,s_1,t_1,u_1,v_1,w_1\right]\times\left[m_2,n_2,o_2,p_2,q_2,r_2,s_2,t_2,u_2,v_2,w_2\right]$는 전체 <span class="__h_hyper">하이퍼 배열</span>의 부분 <span class="__h_hyper">하이퍼 배열</span>이다.</li>
		<li>$1 \le op \le 66$인 연산은 통틀어 최대 $1\,111$개까지만 등장한다.</li>
		<li>입력 형식에서는 $+w$ 방향이 <strong>오른쪽</strong>이지만, 실제 연산 처리에서는 $+w$는 항상 <strong>아래 방향</strong>임에 유의하라.</li>
	</ul>
	</li>
	<li><span style="color:#e74c3c;"><code>op</code></span><br>
	: 전체 <span class="__h_hyper">하이퍼 배열</span>에 대해 연산 $op$를 수행한다. ($67 \le op \le 121$)</li>
</ul>

<p> </p>

### 출력 

 <p>$\rho$개의 연산을 차례대로 수행한 후 최종 결과를 출력한다. 출력 형식은 입력 형식과 같다.</p>

