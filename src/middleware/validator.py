class Validator:
    """
    Capa de Middleware para validar las entradas del usuario antes de
    pasar al Backend.
    """
    
    @staticmethod
    def validar_texto(texto: str) -> tuple[bool, str]:
        """
        Valida que el texto no esté vacío y cumpla con requisitos básicos.
        
        Args:
            texto (str): El texto a validar.
            
        Returns:
            tuple[bool, str]: (Es válido, Mensaje de error si aplica)
        """
        if not texto:
            return False, "El campo de texto no puede estar vacío."
        
        if not isinstance(texto, str):
            return False, "La entrada debe ser texto."
            
        # Aquí se podrían agregar más validaciones si fuera necesario
        # Por ejemplo, limitar la longitud, prohibir ciertos caracteres, etc.
        
        return True, ""
