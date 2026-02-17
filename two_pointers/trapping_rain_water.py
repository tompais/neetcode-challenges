from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        # Inicializamos dos punteros, uno al inicio y otro al final
        left, right = 0, len(heights) - 1
        # Variables para almacenar la altura máxima desde la izquierda y la derecha
        left_max, right_max = 0, 0
        # Variable para acumular el agua total atrapada
        water = 0
        # Recorremos el array mientras los punteros no se crucen
        while left < right:
            # Si la altura en la izquierda es menor
            if heights[left] < heights[right]:
                # Si la altura actual es mayor o igual al máximo izquierdo, actualizamos left_max
                if heights[left] >= left_max:
                    left_max = heights[left]
                else:
                    # Si no, sumamos la diferencia (agua atrapada en esa posición)
                    water += left_max - heights[left]
                left += 1
            else:
                # Si la altura actual es mayor o igual al máximo derecho, actualizamos right_max
                if heights[right] >= right_max:
                    right_max = heights[right]
                else:
                    # Si no, sumamos la diferencia (agua atrapada en esa posición)
                    water += right_max - heights[right]
                right -= 1
        # Devolvemos el total de agua atrapada
        return water

