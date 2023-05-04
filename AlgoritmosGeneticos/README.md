<h1 align="center">🧪 Fundamentos e Experimentos de Algoritmos Genéticos 🧐 </h1>

Para começar o conteúdo, como quando você vai ler um artigo científico, uma tese de uma banca da qual você fará parte ou participar de uma reunião com seu grupo de pesquisa, é válido estar por dentro do tema e entender alguns conceitos, mesmo que básicos, para fornecer uma base. Com isso, ficará mais fácil e fluído o aprendizado e as discussões, bem como formular dúvidas. Se não, como você terá dúvidas se não entender nada?

<h2> O que são algoritmos genéticos? 🤔 </h2>

<blockquote>Essa é uma pergunta totalmente válida, e é necessário conhecer um pouquinho de alguns conceitos que podem facilitar a trajetória por esse ramo da computação.
Podemos separar os termos para facilitar o entendimento: <br>

- **Algoritmo:** Numa consulta rápida a <a href="https://en.wikipedia.org/wiki/Algorithm"> Wikipédia</a>, podemos deduzir que um algoritmo é uma sequência finita de instruções rigorosas, normalmente usadas para resolver uma classe de problemas específicos ou para realizar uma computação. Ainda, são usados como especificações para realizar cálculos e processamento de dados. <br>

- **Genética:** Também consultando a <a href="https://en.wikipedia.org/wiki/Genetics"> Wikipédia</a> vemos que a Genética é o estudo dos genes, variação genética e hereditariedade em organismos. É um ramo importante da biologia porque a hereditariedade é vital para a evolução dos organismos. Atente-se para os termos de variação genética. Essa variação acontece devido a um processo que se chama <a href="https://education.nationalgeographic.org/resource/natural-selection/"> seleção natural</a> que é um fator essencial para a evolução baseado na adaptabilidade dos organismos.

Logo, se juntarmos **Algoritmo + Genética** teremos os **Algoritmos Genéticos**! Uma sequência de instruções que levará um conjunto de "indivíduos", através de uma seleção, para uma espécie de "evolução" onde os mais aptos sobrevivem. Tal qual a realidade, esses algoritmos se baseiam em três pontos principais: seleção, cruzamento e mutação. Por uma sequência de eventos, a melhor genética vencerá.</blockquote>

<h2> Entendi... mas para que isso é útil? 🤔 </h2>

<blockquote>Podemos aplicar um Algoritmo Genético para resolver uma variedade de problemas de otimização que não são adequados para algoritmos de otimização padrão, incluindo problemas nos quais a função objetivo é descontínua, não diferenciável, estocástica, ou altamente não linear (<a href="https://www.mathworks.com/help/gads/what-is-the-genetic-algorithm.html"> MathWorks</a>). Vemos ele é uma ferramente muito poderosa para resolver problemas e, por conta disso, pode ser uma carta na manga para quando você se deparar com uma situação que seus algoritmos tradicionais não consigam dar conta. Abaixo podemos ver uma tabela (traduzida e adaptada de <a href="https://www.mathworks.com/help/gads/what-is-the-genetic-algorithm.html"> MathWorks</a>) que resume as principais diferenças entre os algoritmos tradicionais e genéticos: <br> 
<p align="center">

| Algoritmos Tradicionais | Algoritmos Genéticos |
| ---------------- | ---------------- |
| Gera um único ponto a cada iteração. A sequência de pontos se aproxima de uma solução ótima.  | Gera uma população de pontos a cada iteração. O melhor ponto da população se aproxima de uma solução ótima.  |
| Seleciona o próximo ponto na sequência por um cálculo determinístico. | Seleciona a próxima população por computação que usa geradores de números aleatórios.  |
| Normalmente converge rapidamente para uma solução local.  | Normalmente leva muitas avaliações de função para convergir. Pode ou não convergir para um mínimo local ou global.  |

</p>
</blockquote>

<h2> Agora que conheço esses Algoritmos Genéticos, como eles funcionam? 🤔 </h2>

<blockquote>Vamos aprender nos baseando na biologia. Você verá que no fim as coisas farão sentido. <br>

- **Genótipo:** Na natureza, a reprodução e a mutação ocorrem através do genótipo, que é uma coleção de genes agrupados em cromossomos. Ao reproduzir, os descendentes herdam uma combinação de genes dos pais, através dos cromossomos. Em algoritmos genéticos, essa ideia é imitada, onde cada indivíduo é representado por um cromossomo que contém uma coleção de genes, que pode ser expressa como uma sequência binária; <br>

- **População:** Os algoritmos genéticos mantêm uma população de indivíduos que representam soluções candidatas para um problema. Cada indivíduo é representado por um cromossomo, e a população na totalidade é uma coleção desses cromossomos. A população representa continuamente a geração atual e evolui ao longo do tempo quando a geração atual é substituída por uma nova, por isso, ela é sempre atualizada com novos indivíduos, representando uma nova geração que evolui em relação à anterior; <br>

- **Função _fitness_:** Essa aqui é muito importante! A cada iteração do algoritmo, os indivíduos são avaliados por uma função de _fitness_, sendo essa a função que procuramos otimizar ou o problema que queremos resolver. Os indivíduos com pontuações de fitness mais altas são mais propensos a serem escolhidos para reproduzir e representados na próxima geração, resultando em soluções melhores ao longo do tempo.  Com o tempo, a qualidade das soluções melhora, os valores de _fitness_ aumentam e quando se encontrar uma solução satisfatória, o algoritmo para; <br>

- **Seleção:** A seleção de quais indivíduos na população irão reproduzir e gerar a próxima geração é baseada na pontuação de aptidão. Indivíduos com pontuações mais altas têm uma maior probabilidade de serem selecionados, mas mesmo aqueles com pontuações mais baixas podem ter uma chance, embora menor. Dessa forma, todos os indivíduos contribuem para a evolução da população; <br>

- **_Crossover_:** Para gerar uma nova geração, é comum selecionar dois indivíduos da geração atual como pais e cruzar partes de seus cromossomos para formar dois novos indivíduos. Esse processo é conhecido como cruzamento ou recombinação; <br>

- **Mutação:** A mutação pretende renovar periodicamente e aleatoriamente a população, inserir novos padrões nos cromossomos e incentivar a busca em áreas não exploradas do espaço de solução. A mutação é uma mudança aleatória em um gene que pode ocorrer durante o processo de reprodução. Ela é implementada como uma alteração aleatória em um ou mais valores do cromossomo. <br>

Você pode notar que as coisas seguem uma lógica, muito parecida com a natureza através da seleção natural. Por processos de seleção dos melhores indivíduos (ou parâmetros, por exemplo) chegamos a uma geração de indivíduos evoluídos com as características necessárias para sobreviver onde estão (ou num resultado que foi o melhor para o problema que você propôs). Esses conceitos podem ser melhores esclarecidos, se achar necessário, através do livro <a href="https://www.amazon.com.br/Hands-Genetic-Algorithms-Python-intelligence-ebook/dp/B0842372RQ"> Hands-On Genetic Algorithms with Python</a> e, se facilitar, você pode buscar figuras que ilustram o funcionamento dos Algoritmos Genéticos, como <a href="https://bcc.ime.usp.br/tccs/2003/anselmo/node12.html"> essa</a> no fim do site. <br>

<h2> O que tem nessa pasta? 💻 </h2>

- Algumas coisas que valem a pena aprender ou relembrar.ipynb: Tal qual o título informa, contém algumas informações que podem ajudar no desenvolvimento dos experimentos ✔️;
- README.md - É o arquivo que você está lendo agora ✔️;
- classes.py - Contém algumas classes que serão utilizadas ✔️;
- constantes.py - Contém algumas constantes que serão utilizadas ✔️;
- experimento A.01 - busca aleatoria.ipynb: Experimento sobre Busca Aleatória ✔️;
- experimento A.02 - busca em grade.ipynb: Experimento sobre Busca em Grade ✔️;
- experimento A.03 - algoritmo genetico.ipynb: Primeiro modelo básico de um Algoritmo Genético ✔️;
- experimento A.04 - caixas nao-binarias.ipynb: Segundo modelo básico de um Algoritmo Genético com uma variedade maior de valores que os genes podem assumir ✔️;
- experimento A.05 - descobrindo a senha.ipynb: Experimento utilizando um Algoritmo Genético para descobrir uma senha específica ✔️;
- experimento A.06 - o caixeiro viajante.ipynb: Problema do caixeiro viajante resolvido por busca através de um Algoritmo Genético e busca exaustiva ✔️;
- experimento GA.01 - senha de tamanho variavel.ipynb: Experimento proposto para aplicação dos conceitos estudados para descorbrir uma senha de tamanho variável ✔️;
- experimento A.07 - aplicando restricoes.ipynb: Experimento introduzindo o conceito de "restrição" num código de Algoritmos Genéticos através de um problema simples conhecido como "problema da mochila" ✔️;
- funcoes.py - Funções utilizadas nos experimentos ✔️.

Legenda: <br>
⌛ - O arquivo será atualizado. <br>
✔️ - O arquivo está finalizado.
  
<h2> Considerações finais 😺 </h2>
  
<blockquote> Os experimentos de Algoritmos Genéticos chegeram ao fim! Ao final, aprendemos como criar um Algoritmo Genético básico, entendemos diferenças entre buscas aleatórias e em grade, bem como funciona e como se arquiteta um desses Algoritmos. A maior parte da "base" está nesse repositório, ou seja, essas funções e projetos podem ser usados e adaptados para outros problemas, quem sabe, até mais complexos. Vimos que os Algoritmos Genéticos são muito importantes para otimização, e, também, que podem gerar mutações, que trazem maior heterogeneidade para suas soluções, por isso descobrimos várias senhas nessa jornada! <br> 
