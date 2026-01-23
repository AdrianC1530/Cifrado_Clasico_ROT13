class ROT13Cipher:
    """
    Clase pura que implementa la lógica matemática del cifrado ROT13.
    Utiliza aritmética modular para realizar la sustitución de caracteres.
    """
    
    def procesar(self, texto: str) -> str:
        """
        Aplica el cifrado/descifrado ROT13 al texto de entrada.
        Al ser ROT13 un cifrado involutivo, este mismo método sirve para
        cifrar y descifrar.
        
        Args:
            texto (str): El texto a procesar.
            
        Returns:
            str: El texto resultante.
        """
        resultado = []
        for caracter in texto:
            if 'a' <= caracter <= 'z':
                # (x + 13) mod 26
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
