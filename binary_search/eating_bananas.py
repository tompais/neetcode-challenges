from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Búsqueda binaria sobre la velocidad k
        left, right = 1, max(piles)
        result = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            # Calculamos las horas necesarias para comer todos los montones a velocidad k
            for pile in piles:
                hours += math.ceil(pile / k)
            # Si puede comer en h horas o menos, intentamos una velocidad menor
            if hours <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result

