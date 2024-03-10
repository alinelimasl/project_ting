from ting_file_management.abstract_queue import AbstractQueue
from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._fila = deque()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._fila)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._fila.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        try:
            return self._fila.popleft()
        except IndexError:
            raise IndexError("Fila vazia")

    def search(self, index):
        """Aqui irá sua implementação"""
        if not 0 <= index < len(self):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._fila[index]
