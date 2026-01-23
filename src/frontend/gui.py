import tkinter as tk
from tkinter import messagebox
from src.backend.cipher import ROT13Cipher
from src.middleware.validator import Validator

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Suite de Cifrado Clásico - ROT13")
        self.geometry("600x450")
        self.resizable(False, False)
        
        # Inicializar componentes
        self.cipher = ROT13Cipher()
        self.validator = Validator()
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título
        lbl_titulo = tk.Label(self, text="Cifrado ROT13", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=20)
        
        # Frame principal
        main_frame = tk.Frame(self)
        main_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Entrada
        lbl_entrada = tk.Label(main_frame, text="Texto de Entrada:", font=("Arial", 10))
        lbl_entrada.pack(anchor="w")
        
        self.txt_entrada = tk.Text(main_frame, height=5, font=("Consolas", 10))
        self.txt_entrada.pack(fill="x", pady=(5, 15))
        
        # Opciones (Radio Buttons)
        # Aunque ROT13 es involutivo, agregamos los controles como pide el requerimiento
        self.opcion_var = tk.StringVar(value="Cifrar")
        
        frame_opciones = tk.Frame(main_frame)
        frame_opciones.pack(fill="x", pady=5)
        
        rb_cifrar = tk.Radiobutton(frame_opciones, text="Cifrar", variable=self.opcion_var, value="Cifrar", font=("Arial", 10))
        rb_cifrar.pack(side="left", padx=20)
        
        rb_descifrar = tk.Radiobutton(frame_opciones, text="Descifrar", variable=self.opcion_var, value="Descifrar", font=("Arial", 10))
        rb_descifrar.pack(side="left", padx=20)
        
        # Botón de Acción
        btn_procesar = tk.Button(main_frame, text="Procesar Texto", command=self.procesar, bg="#007bff", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        btn_procesar.pack(pady=15)
        
        # Salida
        lbl_salida = tk.Label(main_frame, text="Resultado:", font=("Arial", 10))
        lbl_salida.pack(anchor="w")
        
        self.txt_salida = tk.Text(main_frame, height=5, font=("Consolas", 10), state="disabled")
        self.txt_salida.pack(fill="x", pady=(5, 0))
        
    def procesar(self):
        texto = self.txt_entrada.get("1.0", "end-1c").strip()
        
        # 1. Validación (Middleware)
        es_valido, mensaje = self.validator.validar_texto(texto)
        
        if not es_valido:
            messagebox.showwarning("Advertencia", mensaje)
            return
            
        # 2. Procesamiento (Backend)
        # ROT13 es simétrico, pero podríamos agregar lógica diferente si fuera otro cifrado
        resultado = self.cipher.procesar(texto)
        
        # 3. Mostrar Resultado
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", "end")
        self.txt_salida.insert("1.0", resultado)
        self.txt_salida.config(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()
