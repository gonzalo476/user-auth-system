"""
Ejemplo de Componentes Reutilizables en PySide6 con arquitectura MVC

Estructura del proyecto:
mi_proyecto/
├── components/          # ⭐ Componentes reutilizables (como en React)
│   ├── __init__.py
│   ├── apple_button.py
│   ├── apple_input.py
│   └── apple_card.py
├── views/              # Vistas que usan los componentes
│   ├── __init__.py
│   └── login_view.py
├── controllers/
│   └── auth_controller.py
├── models/
│   └── user_model.py
└── config/
    └── colors.py
"""

# ============================================================
# config/colors.py
# ============================================================


class AppleColors:
    """Colores del sistema Apple"""

    # Colores primarios
    BLUE = "#007AFF"
    BLUE_HOVER = "#0051D5"
    BLUE_PRESSED = "#004BB8"
    BLUE_DISABLED = "#007AFF80"

    GREEN = "#34C759"
    GREEN_HOVER = "#2AB04A"
    GREEN_PRESSED = "#259A41"

    RED = "#FF3B30"
    RED_HOVER = "#D92A1F"
    RED_PRESSED = "#C0241A"

    GRAY = "#8E8E93"
    GRAY5 = "#E5E5EA"
    GRAY6 = "#F2F2F7"

    # Textos y fondos
    LABEL = "#000000"
    LABEL_SECONDARY = "#3C3C4399"
    BACKGROUND = "#FFFFFF"
    BACKGROUND_SECONDARY = "#F2F2F7"
    SEPARATOR = "#3C3C434A"


# ============================================================
# components/apple_button.py - Botón reutilizable estilo Apple
# ============================================================

from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize, Signal
from config.colors import AppleColors


class AppleButton(QPushButton):
    """
    Botón personalizado estilo Apple - Componente reutilizable

    Similar a un componente de React, acepta props y emite eventos

    Props:
        text: str - Texto del botón
        variant: str - 'primary', 'success', 'danger', 'secondary'
        size: str - 'small', 'medium', 'large'
        full_width: bool - Ocupa todo el ancho disponible

    Signals (como eventos en React):
        clicked - Emitido al hacer click
    """

    def __init__(
        self,
        text="Button",
        variant="primary",
        size="medium",
        full_width=False,
        parent=None,
    ):
        super().__init__(text, parent)

        self.variant = variant
        self.size = size
        self.full_width = full_width

        self._setup_style()
        self._setup_size()

    def _setup_style(self):
        """Configura el estilo según el variant (como props en React)"""

        # Definir colores según variant
        colors = {
            "primary": {
                "normal": AppleColors.BLUE,
                "hover": AppleColors.BLUE_HOVER,
                "pressed": AppleColors.BLUE_PRESSED,
                "disabled": AppleColors.BLUE_DISABLED,
            },
            "success": {
                "normal": AppleColors.GREEN,
                "hover": AppleColors.GREEN_HOVER,
                "pressed": AppleColors.GREEN_PRESSED,
                "disabled": f"{AppleColors.GREEN}80",
            },
            "danger": {
                "normal": AppleColors.RED,
                "hover": AppleColors.RED_HOVER,
                "pressed": AppleColors.RED_PRESSED,
                "disabled": f"{AppleColors.RED}80",
            },
            "secondary": {
                "normal": AppleColors.GRAY5,
                "hover": AppleColors.GRAY,
                "pressed": "#D1D1D6",
                "disabled": f"{AppleColors.GRAY5}80",
            },
        }

        color_set = colors.get(self.variant, colors["primary"])
        text_color = "#FFFFFF" if self.variant != "secondary" else AppleColors.LABEL

        style = f"""
            QPushButton {{
                background-color: {color_set['normal']};
                color: {text_color};
                border: none;
                border-radius: 8px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {color_set['hover']};
            }}
            QPushButton:pressed {{
                background-color: {color_set['pressed']};
            }}
            QPushButton:disabled {{
                background-color: {color_set['disabled']};
                color: {text_color}80;
            }}
        """

        self.setStyleSheet(style)

    def _setup_size(self):
        """Configura el tamaño del botón"""
        sizes = {"small": (80, 32, 12), "medium": (120, 44, 14), "large": (160, 52, 16)}

        min_width, height, font_size = sizes.get(self.size, sizes["medium"])

        if self.full_width:
            self.setMinimumHeight(height)
        else:
            self.setMinimumSize(QSize(min_width, height))

        # Actualizar font-size en el stylesheet
        current_style = self.styleSheet()
        self.setStyleSheet(
            current_style + f"QPushButton {{ font-size: {font_size}px; }}"
        )


# ============================================================
# components/apple_input.py - Input reutilizable estilo Apple
# ============================================================

from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Signal


class AppleInput(QLineEdit):
    """
    Input personalizado estilo Apple - Componente reutilizable

    Props:
        placeholder: str - Texto placeholder
        input_type: str - 'text', 'password', 'email'
        size: str - 'small', 'medium', 'large'

    Signals:
        textChanged - Emitido cuando cambia el texto (como onChange en React)
        returnPressed - Emitido al presionar Enter
    """

    # Custom signal (como createSignal en React)
    valueChanged = Signal(str)

    def __init__(self, placeholder="", input_type="text", size="medium", parent=None):
        super().__init__(parent)

        self.setPlaceholderText(placeholder)
        self.input_type = input_type
        self.size = size

        self._setup_type()
        self._setup_style()
        self._setup_size()

        # Conectar signal interno a signal custom
        self.textChanged.connect(lambda text: self.valueChanged.emit(text))

    def _setup_type(self):
        """Configura el tipo de input"""
        if self.input_type == "password":
            self.setEchoMode(QLineEdit.EchoMode.Password)

    def _setup_style(self):
        """Aplica estilos de Apple"""
        style = f"""
            QLineEdit {{
                background-color: {AppleColors.BACKGROUND};
                border: 1px solid {AppleColors.SEPARATOR};
                border-radius: 8px;
                padding: 0 12px;
                color: {AppleColors.LABEL};
                font-size: 14px;
            }}
            QLineEdit:focus {{
                border: 2px solid {AppleColors.BLUE};
                padding: 0 11px;
            }}
            QLineEdit:disabled {{
                background-color: {AppleColors.GRAY6};
                color: {AppleColors.LABEL_SECONDARY};
            }}
        """
        self.setStyleSheet(style)

    def _setup_size(self):
        """Configura el tamaño"""
        heights = {"small": 32, "medium": 40, "large": 48}
        height = heights.get(self.size, 40)
        self.setMinimumHeight(height)


# ============================================================
# components/apple_card.py - Card container reutilizable
# ============================================================

from PySide6.QtWidgets import QFrame, QVBoxLayout


class AppleCard(QFrame):
    """
    Card contenedor estilo Apple - Componente reutilizable

    Props:
        padding: int - Padding interno
        elevation: bool - Sombra elevada
    """

    def __init__(self, padding=20, elevation=True, parent=None):
        super().__init__(parent)

        self.padding = padding
        self.elevation = elevation

        # Layout interno
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(padding, padding, padding, padding)

        self._setup_style()

    def _setup_style(self):
        """Aplica estilos de card"""
        shadow = "box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);" if self.elevation else ""

        style = f"""
            QFrame {{
                background-color: {AppleColors.BACKGROUND};
                border-radius: 12px;
                border: 1px solid {AppleColors.SEPARATOR};
            }}
        """
        self.setStyleSheet(style)

    def add_widget(self, widget):
        """Helper para añadir widgets al card"""
        self.layout.addWidget(widget)


# ============================================================
# views/login_view.py - Vista usando los componentes
# ============================================================

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from components.apple_button import AppleButton
from components.apple_input import AppleInput
from components.apple_card import AppleCard
from config.colors import AppleColors


class LoginView(QWidget):
    """
    Vista de Login usando componentes reutilizables
    Similar a como usarías componentes en React
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sign In")
        self.setMinimumSize(400, 500)

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Card contenedor (como un componente Container en React)
        card = AppleCard(padding=30, elevation=True)

        # Título
        title = QLabel("Sign In")
        title.setStyleSheet(
            f"""
            font-size: 24px;
            font-weight: 600;
            color: {AppleColors.LABEL};
            margin-bottom: 20px;
        """
        )
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Componentes de input (como <Input /> en React)
        self.username_input = AppleInput(
            placeholder="Username", input_type="text", size="large"
        )

        self.password_input = AppleInput(
            placeholder="Password", input_type="password", size="large"
        )

        # Botón de login (como <Button /> en React)
        self.login_button = AppleButton(
            text="Log In", variant="primary", size="large", full_width=True
        )

        # Botón secundario
        self.register_button = AppleButton(
            text="Create Account", variant="secondary", size="large", full_width=True
        )

        # Conectar eventos (como onClick en React)
        self.login_button.clicked.connect(self._handle_login)
        self.password_input.returnPressed.connect(self._handle_login)

        # Añadir widgets al card
        card.add_widget(title)
        card.add_widget(self.username_input)
        card.add_widget(self.password_input)
        card.layout.addSpacing(12)
        card.add_widget(self.login_button)
        card.layout.addSpacing(8)
        card.add_widget(self.register_button)

        # Añadir card al layout principal
        main_layout.addWidget(card)

        # Estilo de fondo
        self.setStyleSheet(f"background-color: {AppleColors.BACKGROUND_SECONDARY};")

    def _handle_login(self):
        """Handler del evento click (como una función en React)"""
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            # Deshabilitar botón si falta data
            self.login_button.setEnabled(False)
            return

        print(f"Logging in: {username}")
        # Aquí llamarías al controller
        # self.controller.login(username, password)


# ============================================================
# main.py - Ejemplo de uso
# ============================================================

from PySide6.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)

    # Usar la vista con componentes reutilizables
    window = LoginView()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
