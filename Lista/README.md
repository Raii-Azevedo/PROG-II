##Lista de exercícios extraída do livro Algoritmos Estruturados – 
Autor: Harry Farrer e outros – Editora: LTC 3a Ed., Pág 75-86
Obs: em todos os exercícios, considere unidade de entrada como sinônimo de 
teclado e unidade de saída, ou impressora, como sinônimo de vídeo (console).
1.12.1. Fazer um algoritmo que:
- Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. A 
última linha que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule e 
escreva a idade média deste grupo de indivíduos.
1.12.2. Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de 50 
pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- o número de homens;
1.12.3. A conversão de graus Farenheit para centígrados é obtida por
C = 5 x (F - 32)
 9
Fazer um algoritmo que calcule e escreva uma tabela de centígrados em função de graus 
Farenheit, que variam de 50 a 150 de 1 em 1.
1.12.4. Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele 
comercializa. Para isto, mandou digitar uma linha para cada mercadoria com nome, preço de 
compra e preço de venda das mesmas. Fazer um algoritmo que:determine e escreva quantas 
mercadorias proporcionam:
lucro < 10%
10% <= lucro <= 20%
lucro > 20%
determine e escreva o valor total de compra e de venda de todas as mercadorias, assim como 
o lucro total.
Observação: o aluno deve adotar um flag.
1.12.5. Supondo que a população de um país A seja da ordem de 90.000.000 de habitantes 
com uma taxa anual de crescimento de 3% e que a população de um país B seja, 
aproximadamente, de 20.000.000 de habitantes com uma taxa anual de crescimento de 1,5%, 
fazer um algoritmo que calcule e escreva o número de anos necessários para que a população 
do país A ultrapasse ou iguale a população do país B, mantidas essas taxas de crescimento.
1.12.6. Um determinado material radioativo perde metade de sua massa a cada 50 segundos. 
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário para 
que essa massa se torne menor do que 0,5 grama. Escreva a massa inicial, a massa final e o 
tempo calculado em horas, minutos e segundos.
1.12.7. Deseja-se fazer um levantamento a respeito da ausência de alunos à primeira prova 
de Programação de Computadores para cada uma das 14 turmas existentes. Para cada turma, 
é fornecido um conjunto de valores, sendo que os dois primeiros valores do conjunto 
corresponde a identificação da turma (A, ou B, ou C,...) e ao número de alunos matriculados, e 
os demais valores deste conjunto contêm o número de matrícula do aluno e a letra A ou P para 
o caso de o aluno estar ausente ou presente, respectivamente. Fazer um algoritmo que: 
- para cada turma, calcule a porcentagem de ausência e escreva a identificação da
turma e a porcentagem calculada;
- determine e escreva quantas turmas tiveram porcentagem de ausência superior a 5%.
1 de 12
1.12.8. Uma certa firma fez uma pesquisa de mercado para saber se as pessoas gostaram ou 
não de um novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua 
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, fazer um algoritmo 
que calcule e escreva:
- o número de pessoas que responderam sim;
- o número de pessoas que responderam não;
- a porcentagem de pessoas do sexo feminino que responderam sim;
- a porcentagem de pessoas do sexo masculino que responderam não;
1.12.9. Foi feita uma pesquisa para determinar o índice de mortalidade infantil em um certo 
período. Fazer um algoritmo que:
- leia inicialmente o número de crianças nascidas no período;
- leia, em seguida um número indeterminado de linhas, contendo, cada uma, o sexo de uma 
criança morta (masculino, feminino) e o número de meses de vida da criança. A última linha, 
que não entrará nos cálculos, contém no lugar do sexo a palavra “vazio”;
- determine e imprima:
a) a porcentagem de crianças mortas no período;
b) a porcentagem de crianças do sexo masculino mortas no período;
c) a porcentagem de crianças que viveram 24 meses ou menos no período.
1.12.10. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa 
cidade, num determinado dia. Para cada casa visitada, é fornecido o número do canal 
(4,5,7,12) e o número de pessoas que o estavam assistindo naquela casa. Se a televisão 
estivesse desligada, nada era anotado, ou seja, esta casa não entrava na pesquisa. Fazer um 
algoritmo que:
- leia um número indeterminado de dados, sendo que o “FLAG” corresponde ao número do 
canal igual a zero;
- calcule a porcentagem de audiência para cada emissora;
- escreva o número do canal e a sua respectiva porcentagem.
1.12.11. Uma universidade deseja fazer um levantamento a respeito do seu concurso 
vestibular. Para cada curso, é fornecido o seguinte conjunto de valores:
- o código do curso;
- o número de vagas;
- número de candidatos do sexo masculino;
- número de candidatos do sexo feminino;
O último conjunto, para indicar fim de dados, contém o código do curso igual a zero. Fazer um 
algoritmo que:
- calcule escreva, para cada curso, o número de candidatos por vaga e a porcentagem de 
candidatos do sexo feminino (escreva também o código correspondente do curso);
- determine o maior número de candidatos por vaga e escreva esse número juntamente com o 
código do curso correspondente (supor que não haja empate);
- calcule e escreva o total de candidatos;
1.12.12. O sistema de avaliação de uma determinada disciplina obedece aos seguintes 
critérios:
- durante o semestre são dadas três notas;
- a nota final é obtida pela média aritmética das notas dadas durante o curso;
- é considerado aprovado o aluno que obtiver a nota final superior ou igual a 60 e que tiver 
comparecido a um mínimo de 40 aulas.
2 de 12
Fazer um algoritmo que:
a) Leia um conjunto de dados contendo o número de matrícula, as três notas e a frequência
(número de aulas frequentadas) de 100 alunos.
b) Calcule:
- a nota final de cada aluno;
- a maior e menor nota da turma;
- a nota média da turma;
- o total de alunos reprovados;
- a porcentagem de alunos reprovados por infrequência;
c) Escreva:
- para cada aluno, o número de matrícula, a frequência, a nota final e o código (aprovado ou 
reprovado);
- o que foi calculado no item b (2,3,4 e 5).
1.12.13. Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em 
uma determinada cidade. Para isso, são fornecidos os seguintes dados:
- preço do kWh consumido;
- número do consumidor;
- quantidade de kWh consumidos durante o mês;
- código do tipo de consumidor (residencial, comercial, industrial).
O número do consumidor igual a zero deve ser usado como flag. Fazer um algoritmo que:
- leia os dados descritos acima:
- calcule:
a) para cada consumidor, o total a pagar;
b) o maior consumo verificado;
c) o menor consumo verificado;
d) o total do consumo para cada um dos três tipos de consumidores;
e) a média geral de consumo;
- escreva:
a) para cada consumidor, o seu número e o total a pagar;
b) o que foi calculado nos itens b, c, d, e acima especificados.
1.12.14. Tem-se uma estrada ligando várias cidades. Cada cidade tem seu marco 
quilométrico. Fazer um algoritmo que:
- leia vários pares de dados, contendo cada par os valores dos marcos quilométricos, em ordem
crescente, de duas cidades. O último par contém estes dois valores iguais;
- calcule os tempos decorridos para percorrer a distância entre estas duas cidades, com as 
seguintes velocidades: 20, 30, 40, 50, 60, 70, 80 km/hora, sabendo-se que t = e/v ,
onde t = tempo; e = espaço; v = velocidade;
- escreva os marcos quilométricos, a velocidade e o tempo decorrido entre as duas cidades, 
apenas quando este tempo for superior a 2 horas.
1.12.15. Os bancos atualizam diariamente as contas de seus clientes. Essa atualização 
envolve a análise dos depósitos e retiradas de cada conta. Numa conta de balanço mínimo, 
uma taxa de serviço é deduzida se a conta cai abaixo de uma certa quantia especificada. 
Suponha que uma conta particular comece o dia com um balanço de R$ 60,00. O balanço 
mínimo exigido é R$ 30,00 e se o balanço de fim de dia for menor do que isso, uma taxa é 
reduzida da conta.
A fim de que essa atualização fosse feita utilizando computador, é fornecido o seguinte 
conjunto de dados:
3 de 12
- a primeira linha contém o valor do balanço mínimo diário, quantidade de transações e taxa de
serviço;
- as linhas seguintes contém número da conta, valor da transação e código da transação 
(depósito ou retirada);
Escrever um algoritmo que:
- calcule o balanço (saldo/débito) da conta ao fim do dia (se o resultado for negativo, isto 
significa insuficiência de fundos na conta);
- escreva, para cada conta, o seu número e o balanço calculado. Se não houver fundos, 
imprima o número da conta e a mensagem “NÃO HÁ FUNDOS”.
1.12.16. Uma empresa decidiu fazer um levantamento em relação aos candidatos que se 
apresentarem para preenchimento de vagas no seu quadro de funcionários, utilizando 
processamento eletrônico. Supondo que você seja o programador encarregado desse 
levantamento, fazer um algoritmo que:
- leia um conjunto de dados para cada candidato contendo:
a) número de inscrição do candidato;
b) idade;
c) sexo (masculino, feminino);
d) experiência no serviço (sim ou não).
O último conjunto contém o número de inscrição do candidato igual a zero.
- calcule:
a) o número de candidatos do sexo feminino;
b) o número de candidatos do sexo masculino;
c) idade média dos homens com mais de 45 anos entre o total de homens;
d) número de mulheres que têm idade inferior a 35 anos e com experiência no serviço;
e) a menor idade entre mulheres que já tem experiência no serviço;
- escreva:
a) o número de inscrição das mulheres pertencentes ao grupo descrito no item e;
b) o que foi calculado em cada item acima especificado.
1.12.17. Um companhia de teatro planeja dar uma série de espetáculos. A direção calcula 
que, a R$ 5,00 o ingresso, serão vendidos 120 ingressos, e as despesas montarão em R$ 
200,00. A diminuição de R$ 0,50 no preço dos ingressos espera-se que haja um aumento de 26
ingressos vendidos.
Fazer um algoritmo que escreva uma tabela de valores do lucro esperado em função do preço 
do ingresso, fazendo-se varias este preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em R$ 0,50.
Escreva, ainda, o lucro máximo esperado, o preço e o número de ingressos correspondentes.
1.12.18. A comissão organizadora de um rallye automobilístico decidiu apurar os resultados 
da competição através de um processamento eletrônico. Um dos algoritmos necessários para a
classificação das equipes concorrentes é o que emite uma listagem geral do desempenho das 
equipes, atribuindo pontos segundo determinadas normas:
O algoritmo deverá:
a) Ler:
a.1) uma linha contendo os tempos-padrão (em minutos decimais) para as três fases de 
competição;
a.2) um conjunto de linhas contendo cada uma o número de inscrição da equipe e os tempos 
(em minutos decimais) que as mesmas despenderam ao cumprir as três diferentes etapas. A 
última linha (flag), que não entrará nos cálculos, contém o número 9999 como número de 
inscrição.
b) Calcular:
b.1) os pontos de cada equipe em cada uma das etapas, seguindo o seguinte critério:
4 de 12
Seja D o valor absoluto da diferença entre o tempo-padrão (lido na primeira linha) e o tempo 
despendido pela equipe numa etapa:
D < 3 minutos – atribuir 100 pontos à etapa
3 <= D <= 5 minutos – atribuir 80 pontos à etapa
D > 5 minutos – atribuir 80 – (D - 5)/5 pontos à etapa
b.2) o total de pontos de cada equipe nas três etapas;
b.3) a equipe vencedora.
c) Escrever:
c.1) para cada equipe, o número de inscrição, os pontos obtidos em cada etapa e o total de 
pontos obtidos.
1.12.19. Numa certa loja de eletrodomésticos, o comerciário encarregado da seção de 
televisores recebe, mensalmente, um salário fixo mais comissão. Essa comissão é calculada em
relação ao tipo e ao número de televisores vendidos por mês, obedecendo à tabela abaixo:
TIPO N.o DE TELEVISORES
VENDIDOS COMISSÕES
a cores
Maior ou igual a 10
Menor do que 10
R$100,00 por televisor vendido
R$ 50,00 por televisor vendido
Preto e branco Maior ou igual a 20
Menor do que 20
R$ 40,00 por televisor vendido
R$ 20,00 por televisor vendido
Sabe-se, ainda, que ele tem um desconto de 8% sobre seu salário fixo para o INPS. Se o seu 
salário total (fixo + comissões – INPS) for maior ou igual a R$ 3.000,00 ele ainda terá um 
desconto de 5%, sobre esse salário total, relativo ao imposto de renda retido na fonte. 
Sabendo-se que existem 20 empregados nesta seção, leia o valor do salário fixo e, para cada 
comerciário, o número de sua inscrição, o número de televisores a cores e o número de 
televisores preto e branco vendidos; calcule e escreva o número de inscrição de cada 
empregado, seu salário bruto e seu salário líquido.
1.12.20. O dia da semana para uma data qualquer pode ser calculado pela seguinte fórmula: 
Dia da semana = RESTO(QUOCIENTE(2,6 x M – 0,2), 1) + D + A + QUOCIENTE(A,4) + 
QUOCIENTE(S,4) – 2 x S), 7)
Onde:
M – representa o número do mês. Janeiro e fevereiro são os meses 11 e 12do ano
precedente, março é o mês 1 e dezembro é o mês 10;
D – representa o dia do mês;
A – representa o número formado pelos dois últimos algarismos do ano;
S – representa o número formado pelos dois primeiros algarismos do ano;
Os dias da semana são numerados de zero a seis; Domingo corresponde a 0, Segunda a 1, e 
assim por diante.
Fazer um algoritmo que:
- leia um conjunto de 50 datas (dia, mês, ano);
- determine o dia da semana correspondente à data lida, segundo o método especificado;
- escreva, para cada data lida, o dia, mês, ano e o dia da semana calculado.
5 de 12
1.12.21. Numa fábrica trabalham homens e mulheres divididos em três classes:
A – os que fazem até 30 peças por mês;
B – os que fazem de 31 a 35 peças por mês;
C – os que fazem mais de 35 peças por mês;
A classe A recebe salário-mínimo. A classe B recebe salário-mínimo e mais 3% do salário 
mínimo por peça, acima das 30 iniciais. A classe C recebe salário-mínimo e mais 5% do salário 
mínimo por peça acima das 30 iniciais.
Fazer um algoritmo que:
a) leia várias linhas, contendo cada uma:
- o número do operário;
- o número de peças fabricadas por mês;
- o sexo do operário;
b) calcule e escreva
- o salário de cada operário;
- o total da folha mensal de pagamento da fábrica;
- o número total de peças fabricadas por mês;
- a média de peças fabricadas pelos homens em cada classe;
- a média de peças fabricadas pelas mulheres em cada classe;
- o número do operário ou operária de maior salário (não existe empate).
Observação: A última linha, que servirá de flag, terá o número do operário igual a zero.
1.12.22. Uma determinada fábrica de rádios possui duas linhas de montagem distintas: 
standard e luxo. A linha de montagem standard comporta um máximo de 24 operários; cada 
rádio standard dá um lucro de X reais e gasta um homem-dia para sua confecção. A linha de 
montagem luxo comporta no máximo 32 operários; e cada rádio luxo dá um lucro de Y 
cruzados e gasta 2 homens dia para sua confecção. A fábrica possui 40 operários. O mercado é
capaz de absorver toda a produção e o fabricante deseja saber qual esquema de produção a 
adotar de modo a maximizar seu lucro diário.
Fazer um algoritmo que leia os valores de X e Y e escreva, para esse esquema de lucro 
máximo, o número de operários na linha standard e na linha luxo, o número de rádios standard
e luxo produzidos e o lucro.
1.12.23. Fazer um algoritmo para calcular o número de dias decorridos entre duas datas 
(considerar também a ocorrência de anos bissextos), sabendo-se que:
a) cada par de datas é lido numa linha, a última linha contém o número do dia negativo
b) a primeira data na linha é sempre a mais antiga.
O ano está digitado com quatro dígitos.
1.12.24. Fazer um algoritmo que calcule e escreva o valor de S:
S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
1.12.25. Fazer um algoritmo que calcule e escreva a seguinte soma:
2
1
/50 + 22
/49 + 23
/48 + ... + 250/1
1.12.26. Fazer um algoritmo para calcular e escrever a seguinte soma:
S = (37 x 38)/1 + (36 x 37)/2 + (35 x 36)/3 + ... + (1 x 2)/37
1.12.27. Fazer um algoritmo que calcule e escreva o valor de S onde:
S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 ... - 10/100
6 de 12
1.12.28. Fazer um algoritmo que calcule e escreva a soma dos 50 primeiros termos da 
seguinte série:
1000/1 – 997/2 + 994/3 – 991/4 + … 
1.12.29. Fazer um algoritmo que calcule e escreva a soma dos 30 primeiros termos da série:
480/10 - 475/11 + 470/12 – 465/13 + …
1.12.30. Escrever um algoritmo para gerar e escrever uma tabela com s valores do seno de 
um ângulo A em radianos, utilizando a série de Mac-Laurin truncada, apresentada a seguir:
sen A = A – A3
/6 + A5
/120 – A7
/5040
Condições: os valores dos ângulos A devem variar de 0.0 a 6.3, inclusive, de 0.1 em 0.1.
1.12.31. Fazer um algoritmo para calcular e escrever o valor d número p, com precisão de 
0,0001, usando a série:
p = 4 – 4/3 + 4/5 – 4/7 + 4/9 – 4/11 + ...
Para obter a precisão desejada, adicionar apenas os termos cujo valor absoluto seja maior ou 
igual a 0.0001.
1.12.42. Sejam P(x1,y1) e Q(x2,y2) dois pontos quaisquer do plano. A sua distância é dada por
d = Ö(x2 - x1)
2
 + (y2 - y1)
2
Escrever então um algoritmo que, lendo várias linhas onde cada uma contém as coordenadas 
dos dois pontos, escreva para cada par de pontos lidos a sua distância. A última linha contém 
as coordenadas x1, y2, y1, y2 iguais a zero.
1.12.43. A solução x, y para o sistema de equações lineares abaixo:
ax + by = u
cx + dy = v
é dada por:
x = d/(ad - bc) u – b/(ad – bc) v , y = - c/(ad - bc) u + a/(ad - bc) v
Escrever um algoritmo que:
• leia várias linhas, onde cada uma contém os parâmetros a, b, c, d, u, v do sistema (a última 
linha contém os valores a, b, c, d iguais a zero);
• calcule a solução x, y de cada sistema dado por seus parâmetros;
• escreva os parâmetros lidos e os valores calculados.
1.12.44. Fazer um algoritmo que, lendo em uma unidade de entrada os parâmetros A e B de 
uma reta no plano dado pela equação Y = AX + B, determina a área do triângulo formado por 
esta reta e os eixos coordenados.
O algoritmo lerá um número indeterminado de linhas, cada linha contendo um par de 
parâmetros (A, B), e para cada par lido deverá escrever: os parâmetros A e B e a área do 
triângulo.
A execução do algoritmo deverá terminar quando ler uma linha cm um par de zeros. 
Observação: Se, em uma linha (à exceção da última), um dos parâmetros for igual a zero, não 
haverá triângulo – assim, o programa deverá imprimir A, B, e 0 (zero).
7 de 12
1.12.45. Fazer um algoritmo para tabular a função y = f(x) + g(x), para x = 1, 2, 3, ..., 10 
onde:
h(x) = x2 - 16
f(x) = h(x), se h(x) >= 0
= 1, se h(x) < 0
g(x) = x2 + 16, se f(x) = 0
= 0, se f(x) > 0
1.12.46. As coordenadas de um ponto (x,y) estão disponíveis em uma unidade de entrada. Ler
esses valores (até quando um flag ocorrer) e escrever “INTERIOR” se o ponto estiver dentro da 
região hachurada entre as retas mostrada abaixo, (y2 < |y| < y1); caso contrário, escrever 
“EXTERIOR”.
1.12.47. Fazer um algoritmo para calcular e escrever a soma dos cubos dos números pares 
compreendidos entre B e A . Suponha que os valores de B e A (B > A) são dados em uma linha.
1.12.48. Fazer um algoritmo que calcule o volume de uma esfera em função do raio R. O raio 
deverá varias de 0 a 20 cm de 0,5 em 0,5 cm
V = 4/3 p R3
1.12.49. Fazer um algoritmo para calcular e escrever a área de um polígono regular de N lados
inscrito numa circunferência de raio R. O número de polígonos será fornecido na primeira linha 
de dados e nas linhas seguintes serão fornecidos os valores de N e R.
1.12.50. Para um polígono regular inscrito numa circunferência, quanto maior o número de 
lados do polígono, mais seu perímetro se aproxima do comprimento da circunferência. Se o 
número de lados for muito grande e o raio da circunferência for unitário, o semiperímetro do 
polígono terá um valor muito próximo de p.
Fazer um algoritmo que escreva uma tabela do semiperímetro em função do número de lados, 
para polígonos regulares inscritos, numa circunferência de raio unitário. O número de lados 
deverá variar de 5 a 100 de 5 em 5.
1.12.51. Construir uma tabela de perda de carga em tubulações para vazões que variem de 
0,1ℓ / s a 10ℓ / s, de 0,1 em 0,1, através da fórmula de Hanzen-Willians dada abaixo:
J = Q1.85 x 10,643 x D4.87 x C-1.85
onde:
J = perda de carga (m/1000m);
Q = vazão (m3 /s);
D = diâmetro de tubo (m2);
C = coeficiente de rugosidade.
Os valores de D e C serão lidos de uma unidade de entrada. Considerar como flag o valor D = 
0.
8 de 12
1.12.52. Fazer um algoritmo que calcule e escreva o número de grãos de milho que se pode 
colocar num tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros seguintes o 
dobro do quadro anterior.
1.12.53. Um certo aço é classificado de acordo com o resultado de três testes, que devem 
verificar se o mesmo satisfaz às seguintes especificações:
Teste 1 – conteúdo de carbono abaixo de 7%;
Teste 2 – dureza de Rockwell maior que 50;
Teste 3 – resistência à tração maior do que 80.000 psi.
Ao aço é atribuído o grau 10, se passa pelos três testes; 9, se passa apenas nos testes 1 e 2; 8,
se passa no teste 1; e 7, se não passou nos três testes. Supondo que sejam lidos de uma 
unidade de entrada: número de amostra, conteúdo de carbono (em %), a dureza de Rockwell e 
a resistência à tração (em psi) – fazer um algoritmo que dê a classificação de 112 amostras de 
aço que foram testadas, escrevendo o número da amostra e o grau obtido.
1.12.54. Fazer um algoritmo para calcular a raiz quadrada de um número positivo, usando o 
roteiro abaixo, baseado no método de aproximações sucessivas de Newton:
Seja Y o número:
• A primeira aproximação para a raiz quadrada de Y é X1 = Y/2
• as sucessivas aproximações serão: Xn+1 = (Xn
2 + Y)/2Xn
O algoritmo deverá prever 20 aproximações.
1.12.55. Dada a equação x3 - 3x2 + 1 = 0 , pode-se encontrar qualquer uma de suas raízes 
reais através de aproximações sucessivas utilizando a seguinte fórmula:
Xn+1 = Xn – (Xn
3 -3Xn
2 + 1)/(3Xn
2 - 6Xn)
Fazer um algoritmo que:
• considere como primeira aproximação X = 1,5;
• calcule e escreva a trigésima aproximação da raiz.
1.12.56. Fazer um algoritmo que tabule a seguinte função:
f(x,y) = (x2 + 3x + y2) / (xy - 5y - 3x + 15)
para x = 1,4,9,16, ...,100; 
e y = 0,1,2, ...,5 para cada valor de x.
1.12.57. Tem-se 10 conjuntos de valores, onde cada conjunto é formado pelo número de um 
aluno, a nota provisória do seu trabalho prático e a data em que foi entregue.
Fazer um algoritmo para:
a) Calcular e imprimir a nota final de cada aluno, sabendo-se que os trabalhos entregues:
• até 20/04, nota final = nota provisória + 10 pontos;
• até 02/05, nota final = nota provisória;
• até 30/05, nota final = nota provisória/2;
• até 30/06, nota final = 0.
b) Calcular a média e o desvio padrão das notas provisória e final.
Observação: Desvio padrão =
9 de 12
1.12.58. Números complexos podem ser escritos na forma cartesiana Z = x + iy ou na forma 
exponencial Z = re 
iq . Multiplicações e divisões de números complexos na forma exponencial 
ficam muito mais fáceis de serem feitas, pois assumem a seguinte forma:
Z1 x Z2 = r1e 
iq1 x r2e 
iq2 = (r1 x r2)e 
i(q1+ q2)
bastando, portanto, operar os módulos (r1 e r2) e os argumentos (q1 e q2) .
Fazer um algoritmo que leia um conjunto de linhas, cada uma contendo um código de quatro 
valores. Código MULTIPLICA indica que se quer operar a multiplicação dos dois números 
complexos representados pelos quatro valores (r1, q1, r2, q2) . Código DIVIDE indica que a 
operação desejada é a divisão. E código VAZIO vai indicar fim de dados. Para cada operação 
completada, escrever todos os valores lidos e os valores obtidos.
1.12.59. O cálculo do valor de uma integral definida, usando o método das aproximações por 
trapézios, é feito dividindo o intervalo de integração em n partes iguais e aproximando a 
função, em cada subintervalo obtido, por um segmento de reta. O valor da integral é calculado,
então, como a soma das áreas dos diversos trapézios formados.
A = ((yi + yi+1)/2) . h , área de cada trapézio
h = xi+1 - xi = (b – a) / n = constante
Fazer um algoritmo para determinar e escrever o valor de p, o qual pode ser calculado pela 
integral:
p = 4. ∫0
1
1/( 1 + x2) dx
1.12.60. Fazer um algoritmo que:
• leia um conjunto de 25 linhas, contendo, cada uma três números inteiros positivos (em 
qualquer ordem).
• calcule o máximo divisor comum entre os três números lidos, utilizando o método das 
divisões sucessivas.
• escreva os três números lidos e o m.d.c. entre eles.
1.12.61. O número 3025 possui a seguinte característica:
30 + 25 = 55
552 = 3025
Fazer um algoritmo para um programa que pesquise e imprima todos os números de quatro 
algoritmos que apresentam tal característica.
1.12.62. Dada uma equação diferencial y = f(x,y) e a condição inicial y(x0) = y0 pode-se 
encontrar uma solução aproximada desta equação, usando o seguinte método:
y1 = y0 + hf(x0,y0)
y2 = y1 + hf(x1,y1)
:
Yk+1 = yk + hf(xk,yk)
Onde h é um acréscimo que se dá aos valores de x, xn limite superior do intervalo;
h = (xn – x0) / n 
x0 : limite inferior do intervalo;
n : número de subintervalos.
Fazer, portanto, um algoritmo que encontre e escreva as soluções aproximadas da equação y’ 
= xy com y(0) = 1 no intervalo fechado de 0 a 1, com n = 10 subintervalos.
10 de 12
1.12.63. Fazer um algoritmo que:
• calcule o número de divisores dos números compreendidos entre 300 e 400.
• Escreva cada número e o número de divisores correspondentes.
1.12.64. Fazer um algoritmo que, dados 100 números inteiros positivos, calcule e imprima os 
que são números perfeitos.
Nota: Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao 
número.
Exemplo: 6 é perfeito porque 1 + 2 + 3 = 6.
1.12.65. Regressão linear é uma técnica estatística que ajusta uma equação linear (da forma y
= ax + b) a um conjunto de pontos dados. O problema consiste em achar uma equação linear 
que melhor se ajuste aos pontos dados. Um dos métodos empregados é o dos mínimos 
quadrados, que consiste em minimizar a soma dos quadrados dos desvios verticais dos pontos 
para a linha reta.
As fórmulas para os coeficientes a e b, dado um conjunto de n pares de pontos (x,y) são
Uma vez achada a equação da reta, é importante determinar a precisão de ajustamento dessa 
linha aos dados reais. Uma medida disso é o coeficiente de correlação R, dado pela fórmula
O intervalo de variação de R é de –1 <= R <= 1. Quanto mais próximo de 1 ou –1 ficar o valor
de R, melhor terá sido o ajustamento da reta.
Fazer um algoritmo para ler e imprimir um conjunto de pares de pontos (x,y) e calcular e
escrever os valores de a, b e R.
11 de 12
1.12.66. Capicuas são números que têm o mesmo valor, se lidos da esquerda para a direita ou
da direita para a esquerda. Ex: 44, 232, etc.
Fazer um algoritmo que determine e escreva todos os números inteiros menores que 10.000 
que são quadrados perfeitos e capicuas ao mesmo tempo.
1.12.67. Número primo é aquele que só é divisível por ele mesmo e pela unidade. 
Fazer um algoritmo que determine e escreva os números primos compreendidos entre
5.000 e 7.000.
1.12.68. Fazer um algoritmo que:
• leia um conjunto de linhas contendo, cada uma, um número inteiro, na base 10, de até cinco 
dígitos. A última linha contém o valor zero;
• transforme esse número da base 10 para a base 2;
• escreva o número na base 10 e na base 2.
1.12.69. Fazer um algoritmo que:
• leia um conjunto de linhas contendo, cada uma, um número inteiro na base 3. A última linha 
contém o valor zero;
• transforme esse número na base 3 para a base 10;
• escreva o número na base 3 e na base 10.
Fim (por enquanto).
