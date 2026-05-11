"""
PROBLEMA: Reverse Linked List (Easy)
Link: https://leetcode.com/problems/reverse-linked-list/

Dado o head de uma lista ligada, reverta a lista e retorne o novo head.

Exemplo:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1
"""


class ListNode:
    """Nó de uma lista ligada."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    """
    Solução iterativa — O(n) tempo, O(1) espaço.

    Raciocínio:
        Percorremos a lista mantendo três ponteiros:
        - anterior: nó já revertido
        - atual: nó sendo processado
        - proximo: nó a ser processado

        A cada passo, invertemos o ponteiro do nó atual.
    """
    anterior = None
    atual = head

    while atual:
        proximo = atual.next   # salva o próximo antes de sobrescrever
        atual.next = anterior  # inverte o ponteiro
        anterior = atual       # avança o anterior
        atual = proximo        # avança o atual

    return anterior  # novo head é o último nó visitado


# ── Helpers para teste ─────────────────────────────────────
def lista_para_array(head: ListNode) -> list:
    resultado = []
    while head:
        resultado.append(head.val)
        head = head.next
    return resultado


def array_para_lista(arr: list) -> ListNode:
    if not arr:
        return None
    head = ListNode(arr[0])
    atual = head
    for val in arr[1:]:
        atual.next = ListNode(val)
        atual = atual.next
    return head


# ── Testes ────────────────────────────────────────────────
if __name__ == "__main__":
    head = array_para_lista([1, 2, 3, 4, 5])
    assert lista_para_array(reverse_list(head)) == [5, 4, 3, 2, 1]

    head = array_para_lista([1, 2])
    assert lista_para_array(reverse_list(head)) == [2, 1]

    assert reverse_list(None) is None
    print("✅ Todos os testes passaram!")
