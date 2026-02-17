from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creamos un diccionario para contar la frecuencia de cada número
        count = defaultdict(int)
        for num in nums:
            count[num] += 1  # Incrementamos la frecuencia de cada número

        # Creamos los buckets: una lista donde el índice representa la frecuencia
        # El tamaño máximo de frecuencia es len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)  # Colocamos el número en el bucket de su frecuencia

        # Usamos un ciclo while para recolectar los k elementos más frecuentes sin return dentro del for
        res = []
        freq = len(bucket) - 1
        while len(res) < k and freq > 0:
            res.extend(bucket[freq])  # Añadimos todos los números con frecuencia 'freq'
            freq -= 1
        return res[:k]  # Retornamos solo los k elementos más frecuentes
