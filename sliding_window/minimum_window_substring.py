from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        # Contador de caracteres requeridos
        t_count = Counter(t)
        # Contador de caracteres en la ventana actual
        window = defaultdict(int)
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        left = 0
        # Expandimos la ventana con el puntero derecho
        for right, char in enumerate(s):
            window[char] += 1
            # Si el carácter actual cumple la cantidad requerida
            if char in t_count and window[char] == t_count[char]:
                have += 1
            # Cuando la ventana es válida
            while have == need:
                # Actualizamos el resultado si la ventana es más pequeña
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                # Movemos el puntero izquierdo para reducir la ventana
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""

