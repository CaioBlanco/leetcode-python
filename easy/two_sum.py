"""
PROBLEMA: Two Sum (Easy)
Link: https://leetcode.com/problems/two-sum/

Dado um array de inteiros e um alvo, retorne os índices de dois números
que somam ao alvo.

Exemplo:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]  (porque nums[0] + nums[1] = 2 + 7 = 9)

Restrições:
    - Cada entrada tem exatamente uma solução
    - Não pode usar o mesmo elemento duas vezes
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Solução com HashMap — O(n) tempo, O(n) espaço.

    Raciocínio:
        Para cada número, verificamos se o seu complemento (target - num)
        já foi visto antes. Usamos um dicionário para guardar
        {valor: índice} e fazer a busca em O(1).
    """
    vistos = {}  # {valor: índice}

    for i, num in enumerate(nums):
        complemento = target - num

        if complemento in vistos:
            return [vistos[complemento], i]

        vistos[num] = i

    return []  # sem solução (não ocorre pelas restrições do problema)


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("✅ Todos os testes passaram!")
