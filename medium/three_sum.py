"""
PROBLEMA: 3Sum (Medium)
Link: https://leetcode.com/problems/3sum/

Dado um array, encontre todos os triplos únicos que somam zero.

Exemplo:
    Input:  [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Solução com ordenação + dois ponteiros — O(n²) tempo, O(1) espaço extra.

    Raciocínio:
        Ordenamos o array. Para cada número nums[i], usamos dois ponteiros
        (esquerda e direita) para encontrar pares que somem -nums[i].
        Pulamos duplicatas para evitar triplos repetidos.
    """
    nums.sort()
    resultado = []

    for i in range(len(nums) - 2):
        # Pula duplicatas do elemento fixo
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        esquerda = i + 1
        direita = len(nums) - 1

        while esquerda < direita:
            soma = nums[i] + nums[esquerda] + nums[direita]

            if soma == 0:
                resultado.append([nums[i], nums[esquerda], nums[direita]])

                # Pula duplicatas dos ponteiros
                while esquerda < direita and nums[esquerda] == nums[esquerda + 1]:
                    esquerda += 1
                while esquerda < direita and nums[direita] == nums[direita - 1]:
                    direita -= 1

                esquerda += 1
                direita -= 1

            elif soma < 0:
                esquerda += 1
            else:
                direita -= 1

    return resultado


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    print("✅ Todos os testes passaram!")
