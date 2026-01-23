import sys
import os

# Asegurar que el directorio raíz esté en el path para las importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.frontend.gui import App

if __name__ == "__main__":
    app = App()
    app.mainloop()
