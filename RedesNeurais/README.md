<h1 align="center">🧪 Fundamentos e Experimentos de Algoritmos Genéticos 🧠 </h1>

Para começar o conteúdo, como quando você vai ler um artigo científico, uma tese de uma banca da qual você fará parte ou participar de uma reunião com seu grupo de pesquisa, é válido estar por dentro do tema e entender alguns conceitos, mesmo que básicos, para fornecer uma base. Com isso, ficará mais fácil e fluído o aprendizado e as discussões, bem como formular dúvidas. Se não, como você terá dúvidas se não entender nada?

<h2> O que são redes neurais? 🤔 </h2>

<blockquote> xxx <br>

- **Redes:** Numa consulta rápida a <a href="https://en.wikipedia.org/wiki/Algorithm"> Wikipédia</a>, podemos deduzir que um algoritmo é uma sequência finita de instruções rigorosas, normalmente usadas para resolver uma classe de problemas específicos ou para realizar uma computação. Ainda, são usados como especificações para realizar cálculos e processamento de dados. <br>

- **Neurônios:** Também consultando a <a href="https://en.wikipedia.org/wiki/Genetics"> Wikipédia</a> vemos que a Genética é o estudo dos genes, variação genética e hereditariedade em organismos. É um ramo importante da biologia porque a hereditariedade é vital para a evolução dos organismos. Atente-se para os termos de variação genética. Essa variação acontece devido a um processo que se chama <a href="https://education.nationalgeographic.org/resource/natural-selection/"> seleção natural</a> que é um fator essencial para a evolução baseado na adaptabilidade dos organismos.

Logo, se juntarmos **Algoritmo + Genética** teremos os **Algoritmos Genéticos**! Uma sequência de instruções que levará um conjunto de "indivíduos", através de uma seleção, para uma espécie de "evolução" onde os mais aptos sobrevivem. Tal qual a realidade, esses algoritmos se baseiam em três pontos principais: seleção, cruzamento e mutação. Por uma sequência de eventos, a melhor genética vencerá.</blockquote>

<h2> Entendi... mas para que isso é útil? 🤔 </h2>

<blockquote xxxxxx <br> 
<p align="center">

| Algoritmos Tradicionais | Algoritmos Genéticos |
| ---------------- | ---------------- |
| Gera um único ponto a cada iteração. A sequência de pontos se aproxima de uma solução ótima.  | Gera uma população de pontos a cada iteração. O melhor ponto da população se aproxima de uma solução ótima.  |
| Seleciona o próximo ponto na sequência por um cálculo determinístico. | Seleciona a próxima população por computação que usa geradores de números aleatórios.  |
| Normalmente converge rapidamente para uma solução local.  | Normalmente leva muitas avaliações de função para convergir. Pode ou não convergir para um mínimo local ou global.  |

</p>
</blockquote>

<h2> Agora que conheço essas Redes Neurais, como eles funcionam? 🤔 </h2>

<blockquote>Vamos aprender nos baseando na biologia. Você verá que no fim as coisas farão sentido. <br>

- **Genótipo:** Na natureza, a reprodução e a mutação ocorrem através do genótipo, que é uma coleção de genes agrupados em cromossomos. Ao reproduzir, os descendentes herdam uma combinação de genes dos pais, através dos cromossomos. Em algoritmos genéticos, essa ideia é imitada, onde cada indivíduo é representado por um cromossomo que contém uma coleção de genes, que pode ser expressa como uma sequência binária; <br>

Você pode notar que as coisas seguem uma lógica, muito parecida com a natureza através da seleção natural. Por processos de seleção dos melhores indivíduos (ou parâmetros, por exemplo) chegamos a uma geração de indivíduos evoluídos com as características necessárias para sobreviver onde estão (ou num resultado que foi o melhor para o problema que você propôs). Esses conceitos podem ser melhores esclarecidos, se achar necessário, através do livro <a href="https://www.amazon.com.br/Hands-Genetic-Algorithms-Python-intelligence-ebook/dp/B0842372RQ"> Hands-On Genetic Algorithms with Python</a> e, se facilitar, você pode buscar figuras que ilustram o funcionamento dos Algoritmos Genéticos, como <a href="https://bcc.ime.usp.br/tccs/2003/anselmo/node12.html"> essa</a> no fim do site. <br>
</blockquote>

<h2> O que tem nessa pasta? 💻 </h2>
<blockquote>
- Algumas coisas que valem a pena aprender ou relembrar.ipynb: Tal qual o título informa, contém algumas informações que podem ajudar no desenvolvimento dos experimentos ✔️;<br>
- README.md - É o arquivo que você está lendo agora ✔️; <br>
- classes.py - Contém algumas classes que serão utilizadas ✔️; <br>
- constantes.py - Contém algumas constantes que serão utilizadas ✔️; <br>
- experimento A.01 - busca aleatoria.ipynb: Experimento sobre Busca Aleatória ✔️; <br>
- experimento A.02 - busca em grade.ipynb: Experimento sobre Busca em Grade ✔️; <br>
- experimento A.03 - algoritmo genetico.ipynb: Primeiro modelo básico de um Algoritmo Genético ✔️; <br>
- experimento A.04 - caixas nao-binarias.ipynb: Segundo modelo básico de um Algoritmo Genético com uma variedade maior de valores que os genes podem assumir ✔️; <br>
- experimento A.05 - descobrindo a senha.ipynb: Experimento utilizando um Algoritmo Genético para descobrir uma senha específica ✔️; <br>
- experimento A.06 - o caixeiro viajante.ipynb: Problema do caixeiro viajante resolvido por busca através de um Algoritmo Genético e busca exaustiva ✔️; <br>
- experimento GA.01 - senha de tamanho variavel.ipynb: Experimento proposto para aplicação dos conceitos estudados para descorbrir uma senha de tamanho variável ✔️; <br>
- experimento A.07 - aplicando restricoes.ipynb: Experimento introduzindo o conceito de "restrição" num código de Algoritmos Genéticos através de um problema simples conhecido como "problema da mochila" ✔️; <br>
- funcoes.py - Funções utilizadas nos experimentos ✔️.
<br>
<br>
Legenda: <br>
⌛ - O arquivo será atualizado. <br>
✔️ - O arquivo está finalizado.
</blockquote>
  
