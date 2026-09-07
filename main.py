```python
import random


# ============================================================
# BUBBLE SORT
# ============================================================

def bubble_sort(vetor):
    vetor = vetor.copy()

    comparacoes = 0
    trocas = 0

    n = len(vetor)

    for i in range(n - 1):
        houve_troca = False

        for j in range(n - 1 - i):
            comparacoes += 1

            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1
                houve_troca = True

        if not houve_troca:
            break

    return vetor, comparacoes, trocas


# ============================================================
# INSERTION SORT
# ============================================================

def insertion_sort(vetor):
    vetor = vetor.copy()

    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        movimentacoes += 1

        j = i - 1

        while j >= 0:
            comparacoes += 1

            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        vetor[j + 1] = chave
        movimentacoes += 1

    return vetor, comparacoes, movimentacoes


# ============================================================
# SELECTION SORT
# ============================================================

def selection_sort(vetor):
    vetor = vetor.copy()

    comparacoes = 0
    trocas = 0

    n = len(vetor)

    for i in range(n - 1):
        menor = i

        for j in range(i + 1, n):
            comparacoes += 1

            if vetor[j] < vetor[menor]:
                menor = j

        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            trocas += 1

    return vetor, comparacoes, trocas


# ============================================================
# QUICK SORT
# ============================================================

def quick_sort(vetor):
    vetor = vetor.copy()

    comparacoes = 0
    movimentacoes = 0

    def particionar(esquerda, direita):
        nonlocal comparacoes, movimentacoes

        pivo = vetor[direita]
        movimentacoes += 1

        i = esquerda - 1

        for j in range(esquerda, direita):
            comparacoes += 1

            if vetor[j] <= pivo:
                i += 1

                if i != j:
                    vetor[i], vetor[j] = vetor[j], vetor[i]
                    movimentacoes += 2

        if i + 1 != direita:
            vetor[i + 1], vetor[direita] = (
                vetor[direita],
                vetor[i + 1]
            )
            movimentacoes += 2

        return i + 1

    def ordenar(esquerda, direita):
        if esquerda < direita:
            posicao_pivo = particionar(esquerda, direita)

            ordenar(esquerda, posicao_pivo - 1)
            ordenar(posicao_pivo + 1, direita)

    ordenar(0, len(vetor) - 1)

    return vetor, comparacoes, movimentacoes


# ============================================================
# EXECUÇÃO DE UM EXPERIMENTO
# ============================================================

def executar_experimento(vetor):
    vetor_bubble = vetor.copy()
    vetor_insertion = vetor.copy()
    vetor_selection = vetor.copy()
    vetor_quick = vetor.copy()

    resultado_bubble = bubble_sort(vetor_bubble)
    resultado_insertion = insertion_sort(vetor_insertion)
    resultado_selection = selection_sort(vetor_selection)
    resultado_quick = quick_sort(vetor_quick)

    return {
        "bubble_comparacoes": resultado_bubble[1],
        "bubble_trocas": resultado_bubble[2],

        "insertion_comparacoes": resultado_insertion[1],
        "insertion_movimentacoes": resultado_insertion[2],

        "selection_comparacoes": resultado_selection[1],
        "selection_trocas": resultado_selection[2],

        "quick_comparacoes": resultado_quick[1],
        "quick_movimentacoes": resultado_quick[2]
    }


# ============================================================
# TABELA PRINCIPAL
# ============================================================

def imprimir_tabela(resultados):
    print("\n")
    print("=" * 125)
    print("RESULTADOS DOS EXPERIMENTOS")
    print("=" * 125)

    cabecalho = (
        f"{'Tam.':<8}"
        f"{'Bubble Comp.':<16}"
        f"{'Bubble Trocas':<16}"
        f"{'Insertion Comp.':<18}"
        f"{'Insertion Mov.':<18}"
        f"{'Selection Comp.':<18}"
        f"{'Selection Trocas':<19}"
        f"{'Quick Comp.':<15}"
        f"{'Quick Mov.':<15}"
    )

    print(cabecalho)
    print("-" * 125)

    for tamanho, resultado in resultados.items():
        print(
            f"{tamanho:<8}"
            f"{resultado['bubble_comparacoes']:<16}"
            f"{resultado['bubble_trocas']:<16}"
            f"{resultado['insertion_comparacoes']:<18}"
            f"{resultado['insertion_movimentacoes']:<18}"
            f"{resultado['selection_comparacoes']:<18}"
            f"{resultado['selection_trocas']:<19}"
            f"{resultado['quick_comparacoes']:<15}"
            f"{resultado['quick_movimentacoes']:<15}"
        )

    print("=" * 125)


# ============================================================
# DESAFIO ADICIONAL
# ============================================================

def executar_desafio(tamanho=20):
    print("\n")
    print("=" * 100)
    print(f"DESAFIO ADICIONAL - {tamanho} ELEMENTOS")
    print("=" * 100)

    vetor_aleatorio = [random.randint(1, 10000) for _ in range(tamanho)]
    vetor_ordenado = sorted(vetor_aleatorio)
    vetor_inverso = sorted(vetor_aleatorio, reverse=True)

    casos = {
        "Aleatório": vetor_aleatorio,
        "Ordenado": vetor_ordenado,
        "Inverso": vetor_inverso
    }

    for nome, vetor in casos.items():

        resultado = executar_experimento(vetor)

        print(f"\nTipo de vetor: {nome}")
        print("-" * 100)

        print(
            f"Bubble Sort    -> "
            f"Comparações: {resultado['bubble_comparacoes']:<8} "
            f"Trocas: {resultado['bubble_trocas']}"
        )

        print(
            f"Insertion Sort -> "
            f"Comparações: {resultado['insertion_comparacoes']:<8} "
            f"Movimentações: {resultado['insertion_movimentacoes']}"
        )

        print(
            f"Selection Sort -> "
            f"Comparações: {resultado['selection_comparacoes']:<8} "
            f"Trocas: {resultado['selection_trocas']}"
        )

        print(
            f"Quick Sort     -> "
            f"Comparações: {resultado['quick_comparacoes']:<8} "
            f"Movimentações: {resultado['quick_movimentacoes']}"
        )


# ============================================================
# VERIFICAÇÃO DOS ALGORITMOS
# ============================================================

def verificar_ordenacao(vetor):
    return vetor == sorted(vetor)


def testar_algoritmos():
    teste = [9, 4, 7, 2, 8, 1, 5, 3, 6]

    bubble = bubble_sort(teste)[0]
    insertion = insertion_sort(teste)[0]
    selection = selection_sort(teste)[0]
    quick = quick_sort(teste)[0]

    if (
        verificar_ordenacao(bubble)
        and verificar_ordenacao(insertion)
        and verificar_ordenacao(selection)
        and verificar_ordenacao(quick)
    ):
        print("Verificação: todos os algoritmos ordenaram corretamente.")
    else:
        print("Erro: algum algoritmo não ordenou corretamente.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print("=" * 80)
    print("ATIVIDADE PRÁTICA - ANÁLISE DE ALGORITMOS DE ORDENAÇÃO")
    print("=" * 80)

    print("\nCritérios utilizados:")
    print("- Comparações: verificações realizadas entre elementos.")
    print("- Bubble/Selection: cada troca efetiva conta como 1 troca.")
    print("- Insertion: cada atribuição de elemento conta como 1 movimentação.")
    print("- Quick: cada atribuição/troca realizada durante o particionamento")
    print("  conta como movimentação.")

    testar_algoritmos()

    tamanhos = [10, 20, 1000]

    resultados = {}

    print("\nGerando os experimentos...")

    for tamanho in tamanhos:

        # Um único vetor original para cada tamanho
        vetor_original = [
            random.randint(1, 10000)
            for _ in range(tamanho)
        ]

        # Os quatro algoritmos recebem cópias idênticas
        resultado = executar_experimento(vetor_original)

        resultados[tamanho] = resultado

    imprimir_tabela(resultados)

    # ========================================================
    # ANÁLISE AUTOMÁTICA DOS RESULTADOS
    # ========================================================

    print("\n")
    print("=" * 80)
    print("ANÁLISE DOS RESULTADOS")
    print("=" * 80)

    r10 = resultados[10]
    r20 = resultados[20]
    r1000 = resultados[1000]

    # Questão A
    menores_comparacoes_10 = {
        "Bubble Sort": r10["bubble_comparacoes"],
        "Insertion Sort": r10["insertion_comparacoes"],
        "Selection Sort": r10["selection_comparacoes"],
        "Quick Sort": r10["quick_comparacoes"]
    }

    menor_algoritmo = min(
        menores_comparacoes_10,
        key=menores_comparacoes_10.get
    )

    print("\na) Menor número de comparações para 10 elementos:")
    print(
        f"   {menor_algoritmo} - "
        f"{menores_comparacoes_10[menor_algoritmo]} comparações."
    )

    # Questão B
    menores_movimentacoes_10 = {
        "Bubble Sort": r10["bubble_trocas"],
        "Insertion Sort": r10["insertion_movimentacoes"],
        "Selection Sort": r10["selection_trocas"],
        "Quick Sort": r10["quick_movimentacoes"]
    }

    menor_mov = min(
        menores_movimentacoes_10,
        key=menores_movimentacoes_10.get
    )

    print("\nb) Menor número de trocas/movimentações para 10 elementos:")
    print(
        f"   {menor_mov} - "
        f"{menores_movimentacoes_10[menor_mov]} operações."
    )

    # Questão C
    print("\nc) Comparação entre 10 e 20 elementos:")

    for algoritmo, chave in [
        ("Bubble Sort", "bubble_comparacoes"),
        ("Insertion Sort", "insertion_comparacoes"),
        ("Selection Sort", "selection_comparacoes"),
        ("Quick Sort", "quick_comparacoes")
    ]:
        print(
            f"   {algoritmo}: "
            f"{r10[chave]} -> {r20[chave]} comparações."
        )

    print(
        "   O comportamento geral pode ser comparado observando o "
        "crescimento das operações."
    )

    # Questão D
    print("\nd) Ao aumentar para 1.000 elementos:")

    for algoritmo, chave in [
        ("Bubble Sort", "bubble_comparacoes"),
        ("Insertion Sort", "insertion_comparacoes"),
        ("Selection Sort", "selection_comparacoes"),
        ("Quick Sort", "quick_comparacoes")
    ]:
        print(
            f"   {algoritmo}: "
            f"{r20[chave]} -> {r1000[chave]} comparações."
        )

    # Questão E
    print("\ne) Bubble, Insertion e Selection:")
    print(
        "   Apesar de os três apresentarem comportamento O(n²) em "
        "situações típicas, isso não significa que executem exatamente "
        "a mesma quantidade de operações."
    )
    print(
        "   As estratégias utilizadas por cada algoritmo são diferentes, "
        "assim como os dados encontrados durante a execução."
    )

    # Questão F
    crescimentos = {
        "Bubble Sort": (
            r1000["bubble_comparacoes"]
            / max(r20["bubble_comparacoes"], 1)
        ),
        "Insertion Sort": (
            r1000["insertion_comparacoes"]
            / max(r20["insertion_comparacoes"], 1)
        ),
        "Selection Sort": (
            r1000["selection_comparacoes"]
            / max(r20["selection_comparacoes"], 1)
        ),
        "Quick Sort": (
            r1000["quick_comparacoes"]
            / max(r20["quick_comparacoes"], 1)
        )
    }

    maior_crescimento = max(
        crescimentos,
        key=crescimentos.get
    )

    print("\nf) Maior crescimento proporcional nas comparações:")
    print(
        f"   {maior_crescimento} "
        f"(aproximadamente {crescimentos[maior_crescimento]:.2f} vezes)."
    )

    # Questão G
    print("\ng) Diferença do Quick Sort:")
    print(
        "   O Quick Sort apresentou crescimento geralmente menor que "
        "os algoritmos O(n²), especialmente quando o número de elementos "
        "aumentou para 1.000."
    )

    # Questão H
    print("\nh) Coerência com as complexidades teóricas:")
    print(
        "   Sim. Bubble Sort, Insertion Sort e Selection Sort possuem "
        "crescimento quadrático em situações típicas, enquanto o "
        "Quick Sort possui complexidade média O(n log n)."
    )

    # Questão I
    print("\ni) Escolha para milhares de pedidos:")
    print(
        "   Entre os quatro algoritmos analisados, o Quick Sort é uma "
        "boa escolha para grandes volumes de dados, pois seu desempenho "
        "médio é O(n log n), apresentando crescimento geralmente menor "
        "que os algoritmos O(n²)."
    )

    # Desafio
    executar_desafio(20)

    print("\n")
    print("=" * 80)
    print("FIM DO EXPERIMENTO")
    print("=" * 80)


if __name__ == "__main__":
    main()
```

