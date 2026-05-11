"""
PROBLEMA: Best Time to Buy and Sell Stock (Easy)
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Dado um array onde prices[i] é o preço de uma ação no dia i,
retorne o lucro máximo que você pode obter comprando e vendendo uma vez.

Exemplo:
    Input:  [7, 1, 5, 3, 6, 4]
    Output: 5  (compra no dia 1 por 1, vende no dia 4 por 6)

    Input:  [7, 6, 4, 3, 1]
    Output: 0  (preços só caem, melhor não operar)
"""


def max_profit(prices: list[int]) -> int:
    """
    Solução com uma passagem — O(n) tempo, O(1) espaço.

    Raciocínio:
        Mantemos o menor preço visto até agora (melhor dia para comprar).
        Para cada dia, calculamos o lucro se vendêssemos hoje e
        atualizamos o lucro máximo.
    """
    if not prices:
        return 0

    menor_preco = float("inf")
    lucro_maximo = 0

    for preco in prices:
        if preco < menor_preco:
            menor_preco = preco
        elif preco - menor_preco > lucro_maximo:
            lucro_maximo = preco - menor_preco

    return lucro_maximo


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([2, 4, 1]) == 2
    print("✅ Todos os testes passaram!")
