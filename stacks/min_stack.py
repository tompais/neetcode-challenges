from collections import deque

class MinStack:
    def __init__(self):
        # Pila principal para los valores
        self.stack = deque()
        # Pila auxiliar para los mínimos
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)  # Agregamos el valor a la pila principal
        # Si la pila de mínimos está vacía o el nuevo valor es menor o igual al mínimo actual, lo agregamos
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Si no, repetimos el mínimo actual
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()  # Quitamos el valor de la pila principal
        self.min_stack.pop()  # Quitamos el mínimo correspondiente

    def top(self) -> int:
        return self.stack[-1]  # Devolvemos el elemento superior

    def getMin(self) -> int:
        return self.min_stack[-1]  # Devolvemos el mínimo actual

