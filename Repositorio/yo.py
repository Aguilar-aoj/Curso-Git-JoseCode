from typing import TypeVar, List

T = TypeVar('T', int, float, str)

def procesar_lista(lista: List[T] = [1, 2, 3]) -> T:
    return lista[0]

print(procesar_lista())