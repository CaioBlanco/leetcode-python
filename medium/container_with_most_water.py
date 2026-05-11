"""
PROBLEMA: Container With Most Water (Medium)
Link: https://leetcode.com/problems/container-with-most-water/

Dado um array onde height[i] é a altura de uma linha vertical,
encontre as duas linhas que formam o container com mais água.

Exemplo:
    Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49  (linhas nos índices 1 e 8: min(8,7) * (8-1) = 7*7 = 49)
"""


def max_area(height: list[int]) -> int:
    """
    Solução com dois ponteiros — O(n) tempo, O(1) espaço.

    Raciocínio:
        Começamos com os ponteiros nas extremidades (maior largura possível).
        A cada passo, movemos o ponteiro da linha MENOR — porque manter a
        linha maior é a única chance de aumentar a área.
        Guardamos a maior área vista.
    """
    esquerda = 0
    direita = len(height) - 1
    maior_area = 0

    while esquerda < direita:
        largura = direita - esquerda
        altura = min(height[esquerda], height[direita])
        area = largura * altura

        maior_area = max(maior_area, area)

        # Move o ponteiro da linha menor
        if height[esquerda] < height[direita]:
            esquerda += 1
        else:
            direita -= 1

    return maior_area


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("✅ Todos os testes passaram!")
