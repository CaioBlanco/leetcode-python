"""
PROBLEMA: Product of Array Except Self (Medium)
Link: https://leetcode.com/problems/product-of-array-except-self/

Dado um array, retorne um array onde output[i] é o produto de todos
os elementos EXCETO nums[i]. Sem usar divisão!

Exemplo:
    Input:  [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
"""


def product_except_self(nums: list[int]) -> list[int]:
    """
    Solução com prefixo e sufixo — O(n) tempo, O(1) espaço extra.

    Raciocínio:
        Para cada posição i, o produto de todos exceto nums[i] é:
            produto_esquerda[i] * produto_direita[i]

        Fazemos duas passagens:
        1. Esquerda para direita: acumula produto dos elementos à esquerda
        2. Direita para esquerda: multiplica pelo produto dos elementos à direita
    """
    n = len(nums)
    resultado = [1] * n

    # Passagem 1: produto acumulado da esquerda
    prefixo = 1
    for i in range(n):
        resultado[i] = prefixo
        prefixo *= nums[i]

    # Passagem 2: multiplica pelo produto acumulado da direita
    sufixo = 1
    for i in range(n - 1, -1, -1):
        resultado[i] *= sufixo
        sufixo *= nums[i]

    return resultado


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("✅ Todos os testes passaram!")
