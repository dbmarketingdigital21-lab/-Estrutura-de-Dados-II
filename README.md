# Análise de Algoritmos de Ordenação

## Atividade Prática – Estrutura de Dados II

### Situação-problema

Uma central de distribuição recebe diariamente diversos pedidos que precisam ser organizados antes de serem encaminhados para separação e expedição.

Cada pedido possui um código numérico de prioridade, e o sistema precisa ordenar esses códigos do menor para o maior.

Neste projeto são analisados quatro algoritmos de ordenação:

* Bubble Sort
* Insertion Sort
* Selection Sort
* Quick Sort

## Objetivo

Desenvolver um experimento computacional em Python para comparar a quantidade de operações realizadas pelos quatro algoritmos de ordenação conforme aumenta a quantidade de elementos processados.

## Experimentos

Foram utilizados vetores com:

* 10 elementos
* 20 elementos
* 1.000 elementos

Para cada tamanho é gerado um único vetor de números aleatórios.

Em seguida, são criadas quatro cópias idênticas do vetor original. Cada algoritmo recebe uma dessas cópias, garantindo que todos sejam executados com os mesmos dados iniciais.

## Contagem das operações

O experimento contabiliza:

### Comparações

É considerada comparação cada operação utilizada para verificar a relação entre dois elementos durante o processo de ordenação.

### Trocas

No Bubble Sort e no Selection Sort, cada troca efetiva entre dois elementos é contabilizada como uma troca.

### Movimentações

No Insertion Sort, são contabilizadas as atribuições realizadas para deslocar e inserir os elementos.

No Quick Sort, são contabilizadas as movimentações realizadas durante o processo de particionamento.

## Algoritmos

### Bubble Sort

Compara elementos adjacentes e realiza trocas quando eles estão fora de ordem.

Complexidade típica:

**O(n²)**

### Insertion Sort

Percorre os elementos e insere cada elemento na posição correta em relação aos elementos anteriores.

Complexidade típica:

**O(n²)**

### Selection Sort

Procura o menor elemento da parte ainda não ordenada e o coloca na posição correta.

Complexidade típica:

**O(n²)**

### Quick Sort

Utiliza um pivô para dividir o vetor em partes menores e realiza a ordenação recursivamente.

Complexidade média:

**O(n log n)**

## Como executar

É necessário ter o Python instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

O programa realizará automaticamente os experimentos e exibirá os resultados no terminal.

## Estrutura do projeto

```text
-Estrutura-de-Dados-II/
│
├── main.py
├── README.md
└── resultados.txt
```

## Desafio adicional

Além dos vetores aleatórios, o programa também realiza testes utilizando:

1. Vetor aleatório
2. Vetor já ordenado
3. Vetor em ordem inversa

Esses testes permitem analisar se a organização inicial dos dados interfere na quantidade de comparações e movimentações realizadas pelos algoritmos.

## Resultados

Os resultados numéricos obtidos durante a execução do programa são registrados no arquivo:

`resultados.txt`

Os valores podem variar entre execuções porque os vetores utilizados nos experimentos são gerados aleatoriamente.

## Conclusão

O experimento permite observar na prática as diferenças de comportamento entre os algoritmos de ordenação.

Bubble Sort, Insertion Sort e Selection Sort apresentam comportamento quadrático em situações típicas, enquanto o Quick Sort apresenta comportamento médio O(n log n).

Com o aumento da quantidade de elementos, principalmente para 1.000 elementos, torna-se possível perceber de forma mais clara a diferença de crescimento no número de operações realizadas pelos algoritmos.

Para situações envolvendo milhares de pedidos, o Quick Sort tende a ser uma alternativa mais adequada entre os algoritmos estudados, devido ao seu desempenho médio O(n log n).

## Tecnologias utilizadas

* Python 3
* GitHub
* Algoritmos de ordenação
* Estruturas de dados
* Análise de complexidade de algoritmos

````

### Depois de colar

No final da página do GitHub:

**Commit changes → Commit changes**

Aí seu repositório já terá:

```text
📁 -Estrutura-de-Dados-II
   📄 main.py
   📄 README.md
````

Depois vamos fazer o **`resultados.txt`**. Para isso, primeiro execute o `main.py` e me mande o resultado que aparecer.
