"""
PROBLEMA: Valid Parentheses (Easy)
Link: https://leetcode.com/problems/valid-parentheses/

Dada uma string com os caracteres '(', ')', '{', '}', '[', ']',
determine se a string é válida.

Regras:
    - Cada abertura deve ser fechada pelo tipo correto
    - Na ordem correta

Exemplo:
    "()"      → True
    "()[]{}"  → True
    "(]"      → False
    "([)]"    → False
    "{[]}"    → True
"""


def is_valid(s: str) -> bool:
    """
    Solução com pilha (stack) — O(n) tempo, O(n) espaço.

    Raciocínio:
        Usamos uma pilha para guardar os parênteses abertos.
        Para cada fechamento, verificamos se o topo da pilha
        é o par correspondente. Se não for, é inválido.
    """
    pilha = []
    pares = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in "({[":
            # Abertura: empilha
            pilha.append(char)
        else:
            # Fechamento: verifica se o topo é o par correto
            if not pilha or pilha[-1] != pares[char]:
                return False
            pilha.pop()

    # Válido apenas se a pilha estiver vazia no final
    return len(pilha) == 0


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("") == True
    print("✅ Todos os testes passaram!")
