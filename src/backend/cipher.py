class ROT13Cipher:
    """
    Clase que implementa la lógica matemática del cifrado ROT13.
    Utiliza aritmética modular para realizar la sustitución de caracteres.
    """
    
    def encrypt(self, texto: str) -> str:
        """
        Se encarga de cifrar el texto recorriendo cada carácter y aplicando
        la rotación de 13 posiciones.
        """
        resultado = []
        for caracter in texto:
            if 'a' <= caracter <= 'z':
                # (x + 13) mod 26: Aplicamos módulo 26 para que el alfabeto sea circular
                # Cuando llegamos a la Z, volvemos a la A
                nuevo_caracter = chr(((ord(caracter) - ord('a') + 13) % 26) + ord('a'))
                resultado.append(nuevo_caracter)
            elif 'A' <= caracter <= 'Z':
                # (x + 13) mod 26
                nuevo_caracter = chr(((ord(caracter) - ord('A') + 13) % 26) + ord('A'))
                resultado.append(nuevo_caracter)
            else:
                # Mantener caracteres que no son letras
                resultado.append(caracter)
        
        return "".join(resultado)

    def decrypt(self, texto: str) -> str:
        """
        Aplica la misma lógica, porque ROT13 es un algoritmo involutivo.
        """
        return self.encrypt(texto)
