from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Inicializamos dos punteros: uno al inicio y otro al final
        left, right = 0, len(height) - 1
        # Variable para almacenar el área máxima encontrada
        max_area = 0
        # Recorremos el array mientras los punteros no se crucen
        while left < right:
            # Calculamos el área entre las dos líneas actuales
            # El área es la distancia entre punteros multiplicada por la altura mínima
            left_height = height[left]
            right_height = height[right]
            area = (right - left) * min(left_height, right_height)
            # Actualizamos el área máxima si encontramos una mayor
            max_area = max(max_area, area)
            # Movemos el puntero que apunta a la línea más baja
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        # Devolvemos el área máxima encontrada
        return max_area

