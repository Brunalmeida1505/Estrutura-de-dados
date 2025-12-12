class Fila:
    def __init__(self):
        self._items = list()
    def estaVazia(self):
        return len(self) == 0
    def _len_(self):
        return len(self._items)
    def enfileira(self,items):
        self._items.append(item)
    def desinfileira(self):
        assert not self.estaVazia()
        return self._items.pop(0)
