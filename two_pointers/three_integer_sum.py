from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Ordenamos el array para facilitar la búsqueda y evitar duplicados
        nums.sort()
        res = []
        n = len(nums)

        # Iteramos sobre cada número, fijando uno como el primero del triplete
        for i in range(n):
            if i <= 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, n - 1
                # Usamos dos punteros para buscar los otros dos números
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total < 0:
                        # Si la suma es menor que 0, movemos el puntero izquierdo a la derecha
                        left += 1
                    elif total > 0:
                        # Si la suma es mayor que 0, movemos el puntero derecho a la izquierda
                        right -= 1
                    else:
                        # Si encontramos una suma igual a 0, guardamos el triplete
                        res.append([nums[i], nums[left], nums[right]])
                        # Saltamos duplicados para el puntero izquierdo
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Saltamos duplicados para el puntero derecho
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        # Movemos ambos punteros
                        left += 1
                        right -= 1
            # Si es igual al anterior, lo saltamos para evitar duplicados

        return res

