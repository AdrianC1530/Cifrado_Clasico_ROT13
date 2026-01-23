import customtkinter as ctk
from tkinter import messagebox
from src.backend.cipher import ROT13Cipher
from src.middleware.validator import Validator

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Suite de Cifrado Clásico - ROT13")
        self.geometry("700x550")
        self.resizable(False, False)
        
        # Inicializar lógica
        self.cipher = ROT13Cipher()
        self.validator = Validator()
        
        # Grid layout configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Título
        self.grid_rowconfigure(1, weight=1) # Contenido
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # --- Header ---
        self.frame_header = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_header.grid(row=0, column=0, sticky="ew", pady=(20, 10))
        
        self.lbl_titulo = ctk.CTkLabel(
            self.frame_header, 
            text="🔐 Cifrado ROT13", 
            font=ctk.CTkFont(family="Roboto", size=24, weight="bold")
        )
        self.lbl_titulo.pack()
        
        self.lbl_subtitulo = ctk.CTkLabel(
            self.frame_header, 
            text="Criptografía Histórica • Ingeniería Moderna", 
            font=ctk.CTkFont(family="Roboto", size=14),
            text_color="gray"
        )
        self.lbl_subtitulo.pack()
        
        self.lbl_integrantes = ctk.CTkLabel(
            self.frame_header,
            text="Desarrollado por: Mateo • Santiago • Adrián",
            font=ctk.CTkFont(family="Roboto", size=11),
            text_color="gray60"
        )
        self.lbl_integrantes.pack(pady=(2, 0))

        # --- Main Content Frame ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Entrada
        self.lbl_entrada = ctk.CTkLabel(self.main_frame, text="Texto de Entrada:", font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_entrada.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))
        
        self.txt_entrada = ctk.CTkTextbox(self.main_frame, height=100, corner_radius=10)
        self.txt_entrada.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 15))
        
        # Controles (Modo de operación)
        self.lbl_modo = ctk.CTkLabel(self.main_frame, text="Modo de Operación:", font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_modo.grid(row=2, column=0, sticky="w", padx=20, pady=(0, 5))
        
        # Usamos SegmentedButton para un look más moderno que los RadioButtons
        self.modo_var = ctk.StringVar(value="Cifrar")
        self.seg_button = ctk.CTkSegmentedButton(
            self.main_frame, 
            values=["Cifrar", "Descifrar"],
            variable=self.modo_var,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.seg_button.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 20))

        # Botón de Acción
        self.btn_procesar = ctk.CTkButton(
            self.main_frame, 
            text="Ejecutar Procesamiento", 
            command=self.procesar,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            corner_radius=20
        )
        self.btn_procesar.grid(row=4, column=0, sticky="ew", padx=20, pady=(0, 20))
        
        # Salida
        self.lbl_salida = ctk.CTkLabel(self.main_frame, text="Resultado:", font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_salida.grid(row=5, column=0, sticky="w", padx=20, pady=(0, 5))
        
        self.txt_salida = ctk.CTkTextbox(self.main_frame, height=100, corner_radius=10, fg_color=("gray90", "gray20"))
        self.txt_salida.grid(row=6, column=0, sticky="ew", padx=20, pady=(0, 20))
        self.txt_salida.configure(state="disabled")
        
    def procesar(self):
        try:
            # 1. Capturamos el texto ingresado por el usuario
            texto = self.txt_entrada.get("1.0", "end-1c").strip()
            
            # 2. Validación (Middleware): Validamos los datos antes de enviarlos
            # Si hay un error, el Validator lanzará una excepción (ValueError)
            self.validator.validar_texto(texto)
            
            # 3. Procesamiento (Backend): Enviamos el texto al backend para cifrar/descifrar
            modo = self.modo_var.get()
            if modo == "Cifrar":
                resultado = self.cipher.encrypt(texto)
            else:
                resultado = self.cipher.decrypt(texto)
            
            # 4. Mostrar Resultado: Mostramos el texto cifrado/descifrado en la interfaz
            self.txt_salida.configure(state="normal")
            self.txt_salida.delete("1.0", "end")
            self.txt_salida.insert("1.0", resultado)
            self.txt_salida.configure(state="disabled")
            
        except ValueError as error:
            # Manejo de errores: Capturamos la excepción y mostramos el mensaje
            messagebox.showwarning("Advertencia", str(error))
        except Exception as e:
            messagebox.showerror("Error Crítico", f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
