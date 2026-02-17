from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Si s1 es más largo que s2, no puede haber permutación
        len1 = len(s1)
        len2 = len(s2)
        is_included = False

        if len1 <= len2:
            # Contador de caracteres de s1
            s1_count = Counter(s1)
            # Contador de la ventana actual en s2
            window = Counter(s2[:len1])
            # Si la primera ventana ya es una permutación
            is_included = window == s1_count
            # Deslizamos la ventana sobre s2
            i = len1
            while i < len2 and not is_included:
                # Agregamos el nuevo carácter a la ventana
                window[s2[i]] += 1
                # Quitamos el carácter que sale de la ventana
                window[s2[i - len1]] -= 1
                # Si el conteo llega a cero, lo eliminamos para mantener la comparación limpia
                if window[s2[i - len1]] == 0:
                    del window[s2[i - len1]]
                # Comparamos los contadores
                is_included = window == s1_count
                i += 1
        return is_included

