from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # Inicializamos el resultado con 1s

        # Paso 1: Producto de todos los elementos a la izquierda de i
        left = 1
        for i in range(n):
            res[i] = left  # Guardamos el producto acumulado a la izquierda
            left *= nums[i]  # Actualizamos el producto acumulado

        # Paso 2: Producto de todos los elementos a la derecha de i
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right  # Multiplicamos por el producto acumulado a la derecha
            right *= nums[i]  # Actualizamos el producto acumulado

        return res  # Devolvemos el resultado final
