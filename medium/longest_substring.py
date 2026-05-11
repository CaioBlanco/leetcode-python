"""
PROBLEMA: Longest Substring Without Repeating Characters (Medium)
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Dada uma string, encontre o comprimento da maior substring sem caracteres repetidos.

Exemplo:
    "abcabcbb" → 3  (substring "abc")
    "bbbbb"    → 1  (substring "b")
    "pwwkew"   → 3  (substring "wke")
"""


def length_of_longest_substring(s: str) -> int:
    """
    Solução com janela deslizante (sliding window) — O(n) tempo, O(n) espaço.

    Raciocínio:
        Mantemos uma janela [esquerda, direita] sem caracteres repetidos.
        Usamos um set para verificar repetições em O(1).
        Quando encontramos um repetido, movemos a esquerda até removê-lo.
    """
    caracteres = set()
    esquerda = 0
    maximo = 0

    for direita in range(len(s)):
        # Se o caractere já está na janela, encolhe pela esquerda
        while s[direita] in caracteres:
            caracteres.remove(s[esquerda])
            esquerda += 1

        caracteres.add(s[direita])
        maximo = max(maximo, direita - esquerda + 1)

    return maximo


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("au") == 2
    print("✅ Todos os testes passaram!")
