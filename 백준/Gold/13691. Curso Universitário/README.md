# [Gold III] Curso Universitário - 13691 

[문제 링크](https://www.acmicpc.net/problem/13691) 

### 성능 요약

메모리: 35508 KB, 시간: 40 ms

### 분류

그래프 이론, 위상 정렬, 방향 비순환 그래프

### 제출 일자

2025년 4월 4일 09:55:20

### 문제 설명

<p>Há alguns anos atrás, a Universidade de Pinguinhos introduziu um novo sistema flexível de créditos para os alunos ingressantes de cursos de graduação. No novo sistema os alunos podem escolher as disciplinas que desejam cursar em um semestre, com a unica restrição de não poderem cursar uma dada disciplina A sem antes terem cursado todas as disciplinas que tiverem sido estabelecidas como pré-requisitos de A. Após alguns semestres o reitor notou que muitos estudantes estavam sendo reprovados em muitas disciplinas, simplesmente porque os estudantes estavam cursando muitas disciplinas por semestre – alguns estudantes chegavam a se matricular em até quinze disciplinas em um semestre. Sendo muito sábio, este ano o reitor introduziu uma regra adicional limitando o número de disciplinas que cada estudante pode cursar por semestre a um certo valor N . Essa regra adicional, no entanto, fez com que os alunos ficassem muito confusos na hora de escolher as disciplinas a serem cursadas em cada semestre.</p>

<p>É aí que você entra na estória. O reitor resolveu disponibilizar um programa de computador para ajudar os alunos a fazerem suas escolhas de disciplinas, e solicitou sua ajuda. Mais precisamente, o reitor quer que o programa sugira as disciplinas a serem cursadas durante o curso da seguinte forma. A cada disciplina é atribuída uma prioridade. Se mais do que N disciplinas podem ser cursadas em um determinado semestre (obedecendo ao sistema de pré- requisitos), o programa deve sugerir que o aluno matricule-se nas N disciplinas de maior prioridade. Se N ou menos disciplinas podem ser cursadas em um determinado semestre, o programa deve sugerir que o aluno matricule-se em todas as disciplinas disponíveis.</p>

<p>Portanto, dadas a descrição de pré-requisitos para cada disciplina, a prioridade de cada disciplina, e o número máximo de disciplinas por semestre, seu programa deve calcular o número necessário de semestres para concluir o curso, segundo a sugestão do reitor, e a lista de disciplinas que o aluno deve matricular-se em cada semestre.</p>

### 입력 

 <p>A entrada contém vários casos de teste. Se uma disciplina não tem qualquer pré-requisito ela é denominada básica; caso contrário ela é denominada avançada. A primeira linha de um caso de teste contém dois inteiros 1 ≤ N ≤ 100 e 1 ≤ M ≤ 10 indicando respectivamente o número de disciplinas avançadas do curso e o número máximo de disciplinas que podem ser cursadas por semestre. Cada uma das N linhas seguintes tem o formato</p>

<p>STR0 K STR1 STR2 ... STRK</p>

<p>onde STR0 é o nome de uma disciplina avançada, 1 ≤ K ≤ 15 é o número de disciplinas que são pré-requisitos de STR0, e STR1, STR2, . . . STRK são os nomes das disciplinas que são pré-requisitos de STR0. O nome de uma disciplina é uma cadeia com no mínimo um e no máximo sete caracteres alfanuméricos maiúsculos (‘A’-‘Z’ e ‘0’-‘9’). Note que as disciplinas básicas são aquelas que aparecem apenas como pré-requisito de alguma disciplina avançada. Para concluir o curso, um aluno deve cursar (e passar!) todas as disciplinas básicas e avançadas. A prioridade das disciplinas é determinada pela ordem em que elas aparecem pela primeira vez na entrada: a que aparece primeiro tem maior prioridade, e a que aparece por último tem a menor prioridade. Não há circularidade nos pré-requisitos (ou seja, se a disciplina B tem como pré-requisito a disciplina A então A não tem B como pré-requisito, direta ou indiretamente). O número total de disciplinas é no máximo igual a 200. O final da entrada é indicado por N = M = 0.</p>

### 출력 

 <p>Para cada caso de teste da entrada seu programa deve produzir a saída na seguinte forma. A primeira linha deve conter a frase ‘Formatura em S semestres’, onde S é o número de semestres necessários para concluir o curso segundo a sugestão do reitor. As S linhas seguintes devem conter a descrição das disciplinas a serem cursadas em cada semestre, um semestre por linha, no formato mostrado no exemplo de saída abaixo. Para cada semestre, a lista das disciplinas deve ser dada em ordem lexicográfica.</p>

<p>Definição: considere as cadeias de caracteres S<sub>a</sub> = a<sub>1</sub>a<sub>2</sub>…a<sub>m</sub> e S<sub>b</sub> = b<sub>1</sub>b<sub>2</sub>…b<sub>n</sub>. S<sub>a</sub> precede S<sub>b</sub> em ordem lexicográfica se e apenas se S<sub>b</sub> é não-vazia e uma das seguintes condições é verdadeira: </p>

<ul>
	<li>S<sub>a</sub> é uma cadeia vazia; </li>
	<li>a<sub>1</sub> < b<sub>1</sub> na ordem ‘0 < ‘1 < ‘2 < … < ‘9 < ‘A < ‘B < … < ‘Z ;</li>
	<li>a<sub>1</sub> = b<sub>1</sub> e a cadeia a<sub>2</sub>a<sub>3</sub>…a<sub>m</sub> precede a cadeia b<sub>2</sub>b<sub>3</sub>…b<sub>n</sub>.</li>
</ul>

