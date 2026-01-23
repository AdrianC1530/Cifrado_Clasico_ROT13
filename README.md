# 🔐 Suite de Cifrado Clásico: ROT13

**Una implementación moderna y arquitectónica del cifrado histórico.**

Este proyecto no es solo una herramienta de cifrado; es una demostración de ingeniería de software aplicada. Diseñado bajo una **Arquitectura de 3 Capas** estricta, separa la lógica matemática pura de la interfaz de usuario, garantizando un código limpio, modular y escalable.

---

## 🌟 Características Destacadas

### 🏛️ Arquitectura Robusta
Diseño "End-to-End" que respeta el patrón **Separation of Concerns**:
*   **Backend Puro:** Lógica matemática aislada y testearle.
*   **Middleware Inteligente:** Capa de validación que protege el núcleo de errores.
*   **Frontend Desacoplado:** Interfaz gráfica independiente y reactiva.

### 🧮 Matemática Modular
Implementación precisa del algoritmo **ROT13** utilizando aritmética modular `(x + 13) mod 26`. Aprovechamos la propiedad **involutiva** del algoritmo: ¡la misma función cifra y descifra!

### 🎨 Interfaz Intuitiva
Una GUI construida con **Tkinter** que ofrece una experiencia de usuario fluida, con controles claros (Radio Buttons) y feedback inmediato.

---

## 🛠️ Stack Tecnológico

Este proyecto ha sido construido utilizando estándares de desarrollo profesional:

*   **Lenguaje:** 🐍 Python 3.x
*   **GUI:** 🖥️ Tkinter (Biblioteca estándar de Python)
*   **Arquitectura:** 🏗️ 3-Tier Architecture (Backend, Middleware, Frontend)
*   **Control de Versiones:** 🐙 Git

---

## 🚀 Instalación y Uso

### Prerrequisitos
*   Python 3.x instalado en tu sistema.

### Despliegue Rápido

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/AdrianC1530/Cifrado_Clasico_ROT13.git
    cd Cifrado_Clasico_ROT13
    ```

2.  **Ejecutar la aplicación:**
    Simplemente corre el archivo principal desde la raíz del proyecto:
    ```bash
    python main.py
    ```

---

## 📄 Estructura del Proyecto

```text
Cifrado_Clasico_ROT13/
├── 📂 src/
│   ├── 📂 backend/     # 🧠 Lógica pura del cifrado (ROT13)
│   ├── 📂 middleware/  # 🛡️ Validaciones y seguridad
│   └── 📂 frontend/    # 🎨 Interfaz Gráfica (GUI)
├── 📄 main.py          # 🏁 Punto de entrada
└── 📄 README.md        # 📖 Documentación
```

---

## 👤 Autor

Hecho con ❤️ y ☕ por **Adrian Carrillo**.
