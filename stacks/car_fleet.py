from typing import List
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Emparejamos posición y velocidad, y ordenamos por posición descendente
        cars = sorted(zip(position, speed), reverse=True)
        stack = deque()  # Pila para los tiempos de llegada de las flotas

        for pos, spd in cars:
            time = (target - pos) / spd  # Tiempo para llegar al objetivo
            # Si la pila está vacía o el tiempo actual es mayor que el de la cima, es una nueva flota
            if not stack or time > stack[-1]:
                stack.append(time)
            # Si no, el auto se une a la flota anterior (no agregamos nada)
        return len(stack)  # El número de flotas es el tamaño de la pila
