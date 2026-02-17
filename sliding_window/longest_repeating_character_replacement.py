from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Diccionario para contar la frecuencia de caracteres en la ventana
        count = defaultdict(int)
        # Puntero izquierdo de la ventana
        left = 0
        # Máxima frecuencia de un solo carácter en la ventana
        max_count = 0
        # Resultado final
        result = 0

        # Recorremos la cadena con el puntero derecho
        for right in range(len(s)):
            # Incrementamos el contador del carácter actual
            count[s[right]] += 1
            # Actualizamos la máxima frecuencia en la ventana
            max_count = max(max_count, count[s[right]])

            # Si la cantidad de reemplazos necesarios supera k, movemos el puntero izquierdo
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Actualizamos el resultado con el tamaño máximo de ventana válido
            result = max(result, right - left + 1)

        return result
