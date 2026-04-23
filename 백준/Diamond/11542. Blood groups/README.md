# [Diamond V] Blood groups - 11542 

[문제 링크](https://www.acmicpc.net/problem/11542) 

### 성능 요약

메모리: 128724 KB, 시간: 1332 ms

### 분류

그래프 이론, 최대 유량, 최소 비용 최대 유량, 서큘레이션

### 제출 일자

2026년 4월 23일 14:59:07

### 문제 설명

<p>There are four possible blood groups for humans: AB, A, B and O, meaning that the red blood cells have antigens of types, respectively, A and B, only A, only B, and no antigen at all. Our blood group is determined by two alleles in our DNA. Each allele is of type either A, B or O. The following table lists the possible allele combinations someone may have for each blood group:</p>

<table class="table table-bordered" style="width:40%">
	<tbody>
		<tr>
			<th>Blood group</th>
			<td>AB</td>
			<td>A</td>
			<td>B</td>
			<td>O</td>
		</tr>
		<tr>
			<th>Possible alleles</th>
			<td>AB</td>
			<td>OA,AA</td>
			<td>OB,BB</td>
			<td>OO</td>
		</tr>
	</tbody>
</table>

<p>We inherit exactly one allele from each of our two parents. So, given the blood groups of the two parents, we can say for sure if some blood group is possible, or not, in their offspring. For example, if the blood groups of the two parents are AB and B, then the possible allele combinations for them are, respectively, {AB} and {OB,BB}. Since the order of the alleles does not matter, the possible allele combinations for the offspring are {OA,AB,OB,BB}. That means the blood groups AB, A and B are possible in their offspring, but the blood group O is not. Very nice indeed! But what if life on Earth had evolved so that a person had three parents, three alleles, and three different antigen types? The allele combinations would look like this:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>Blood group</th>
			<td>ABC</td>
			<td>AB</td>
			<td>AC</td>
			<td>BC</td>
			<td>A</td>
			<td>B</td>
			<td>C</td>
			<td>O</td>
		</tr>
		<tr>
			<th>Possible alleles</th>
			<td>ABC</td>
			<td>OAB,AAB,ABB</td>
			<td>OAC,AAC,ACC</td>
			<td>OBC,BBC,BCC</td>
			<td>OOA,OAA,AAA</td>
			<td>OOB,OBB,BBB</td>
			<td>OOC,OCC,CCC</td>
			<td>OOO</td>
		</tr>
	</tbody>
</table>

<p>If the blood groups of the three parents are A, BC and O, then all blood groups are possible in their offspring, except groups BC and ABC.</p>

<p>The universe is vast! There may be, out there in space, some form of life whose individuals have N parents, N alleles, and N different antigen types. Given the blood groups for the N parents, and a list of Q blood groups to test, your program has to determine which ones are possible, and which ones are not, in the offspring of the given parents.</p>

### 입력 

 <p>The first line contains two integers N and Q, representing respectively the number of parents (and alleles, and antigen types) and the number of queries (1 ≤ N ≤ 100 and 1 ≤ Q ≤ 40). Each of the next N lines describes the blood group of a parent. After that, each of the next Q lines describes a blood group to test. Antigen types are identified with distinct integers from 1 to N, not letters. Each line describing a blood group contains an integer B indicating the number of antigen types in the blood group (0 ≤ B ≤ N), followed by B different integers C<sub>1</sub>, C<sub>2</sub>, . . . , C<sub>B</sub> representing the antigen types present in the blood group (1 ≤ C<sub>i</sub> ≤ N for i = 1, 2, . . . , B).</p>

### 출력 

 <p>For each of the Q queries, output a line with the uppercase letter “Y” if the corresponding blood group is possible in the offspring of the given parents; otherwise output the uppercase letter “N”. Write the results in the same order that the queries appear in the input.</p>

