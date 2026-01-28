from tkinter import messagebox

class Validator:
    """
    Capa de Middleware para validar las entradas del usuario antes de
    pasar al Backend.
    """
    
    @staticmethod
    def validar_texto(texto: str) -> bool:
        """
        Valida que el texto no esté vacío y cumpla con requisitos básicos.
        Si hay un error, muestra un popup y retorna False.
        
        Args:
            texto (str): El texto a validar.
            
        Returns:
            bool: True si es válido, False si hay error.
        """
        try:
            if not texto:
                # Validamos que el dato no sea vacío
                raise ValueError("El campo de texto no puede estar vacío.")
            
            if not isinstance(texto, str):
                raise ValueError("La entrada debe ser texto.")
                
            # Aquí se podrían agregar más validaciones si fuera necesario
            return True

        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado en validación: {e}")
            return False
