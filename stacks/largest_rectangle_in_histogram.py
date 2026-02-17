from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()  # Pila para guardar los índices de las barras
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # Usamos 0 como altura ficticia al final para vaciar la pila
            curr_height = 0 if i == n else heights[i]
            # Mientras la pila no esté vacía y la altura actual sea menor que la de la cima
            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]  # Altura de la barra a procesar
                # Si la pila está vacía, el ancho es i; si no, es i - stack[-1] - 1
                w = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, h * w)  # Actualizamos el área máxima
            stack.append(i)  # Agregamos el índice actual a la pila

        return max_area  # Devolvemos el área máxima encontrada

