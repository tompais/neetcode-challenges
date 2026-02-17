from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n  # Inicializamos el resultado con ceros
        stack = deque()  # Pila (deque) para guardar los índices de los días

        for i, temp in enumerate(temperatures):
            # Mientras la pila no esté vacía y la temperatura actual sea mayor que la del día en la cima de la pila
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()  # Sacamos el índice del día anterior
                res[prev_i] = i - prev_i  # Calculamos cuántos días hay que esperar
            stack.append(i)  # Agregamos el índice del día actual a la pila

        return res  # Devolvemos el resultado final
