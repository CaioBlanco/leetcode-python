"""
PROBLEMA: Palindrome Number (Easy)
Link: https://leetcode.com/problems/palindrome-number/

Dado um inteiro, retorne True se ele for um palíndromo (igual de frente
e de trás).

Exemplo:
    Input:  121   → Output: True
    Input:  -121  → Output: False (negativo nunca é palíndromo)
    Input:  10    → Output: False
"""


def is_palindrome(x: int) -> bool:
    """
    Solução sem converter para string — O(log n) tempo, O(1) espaço.

    Raciocínio:
        Números negativos e múltiplos de 10 (exceto 0) nunca são palíndromos.
        Revertemos apenas a metade direita do número e comparamos com a esquerda.
        Isso evita overflow em linguagens com inteiros fixos.
    """
    # Casos especiais
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    metade_revertida = 0

    # Reverte a metade direita até ela ser >= metade esquerda
    while x > metade_revertida:
        metade_revertida = metade_revertida * 10 + x % 10
        x //= 10

    # Para número par de dígitos: x == metade_revertida
    # Para número ímpar de dígitos: descartamos o dígito do meio com // 10
    return x == metade_revertida or x == metade_revertida // 10


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert is_palindrome(121) == True
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False
    assert is_palindrome(0) == True
    assert is_palindrome(1221) == True
    print("✅ Todos os testes passaram!")
