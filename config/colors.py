"""
Apple UI Colors - Solo Hexadecimales
Colores del sistema de diseño de Apple en formato hex
"""


class AppleColors:
    """Colores de Apple en formato hexadecimal"""

    # ==================== COLORES DEL SISTEMA ====================

    # Azul (System Blue)
    BLUE = "#007AFF"
    BLUE_LIGHT = "#0A84FF"
    BLUE_DARK = "#0A84FF"

    # Verde (System Green)
    GREEN = "#34C759"
    GREEN_LIGHT = "#30D158"
    GREEN_DARK = "#30D158"

    # Índigo (System Indigo)
    INDIGO = "#5856D6"
    INDIGO_LIGHT = "#5E5CE6"
    INDIGO_DARK = "#5E5CE6"

    # Naranja (System Orange)
    ORANGE = "#FF9500"
    ORANGE_LIGHT = "#FF9F0A"
    ORANGE_DARK = "#FF9F0A"

    # Rosa (System Pink)
    PINK = "#FF2D55"
    PINK_LIGHT = "#FF375F"
    PINK_DARK = "#FF375F"

    # Morado (System Purple)
    PURPLE = "#AF52DE"
    PURPLE_LIGHT = "#BF5AF2"
    PURPLE_DARK = "#BF5AF2"

    # Rojo (System Red)
    RED = "#FF3B30"
    RED_LIGHT = "#FF453A"
    RED_DARK = "#FF453A"

    # Verde azulado (System Teal)
    TEAL = "#5AC8FA"
    TEAL_LIGHT = "#64D2FF"
    TEAL_DARK = "#64D2FF"

    # Amarillo (System Yellow)
    YELLOW = "#FFCC00"
    YELLOW_LIGHT = "#FFD60A"
    YELLOW_DARK = "#FFD60A"

    # Menta (System Mint) - Nuevo en iOS 15+
    MINT = "#00C7BE"
    MINT_LIGHT = "#63E6E2"
    MINT_DARK = "#63E6E2"

    # Cian (System Cyan) - Nuevo en iOS 15+
    CYAN = "#32ADE6"
    CYAN_LIGHT = "#64D2FF"
    CYAN_DARK = "#64D2FF"

    # Marrón (System Brown)
    BROWN = "#A2845E"
    BROWN_LIGHT = "#AC8E68"
    BROWN_DARK = "#AC8E68"

    # ==================== GRISES DEL SISTEMA ====================

    # Grises modo claro
    GRAY = "#8E8E93"
    GRAY2 = "#AEAEB2"
    GRAY3 = "#C7C7CC"
    GRAY4 = "#D1D1D6"
    GRAY5 = "#E5E5EA"
    GRAY6 = "#F2F2F7"

    # Grises modo oscuro
    GRAY_DARK = "#8E8E93"
    GRAY2_DARK = "#636366"
    GRAY3_DARK = "#48484A"
    GRAY4_DARK = "#3A3A3C"
    GRAY5_DARK = "#2C2C2E"
    GRAY6_DARK = "#1C1C1E"

    # ==================== COLORES DE ETIQUETA ====================

    # Etiquetas modo claro
    LABEL = "#000000"
    LABEL_SECONDARY = "#3C3C4399"  # 60% opacidad
    LABEL_TERTIARY = "#3C3C434D"  # 30% opacidad
    LABEL_QUATERNARY = "#3C3C432E"  # 18% opacidad

    # Etiquetas modo oscuro
    LABEL_DARK = "#FFFFFF"
    LABEL_SECONDARY_DARK = "#EBEBF599"  # 60% opacidad
    LABEL_TERTIARY_DARK = "#EBEBF54D"  # 30% opacidad
    LABEL_QUATERNARY_DARK = "#EBEBF52E"  # 18% opacidad

    # ==================== COLORES DE RELLENO ====================

    # Rellenos modo claro
    FILL = "#78788033"  # 20% opacidad
    FILL_SECONDARY = "#78788029"  # 16% opacidad
    FILL_TERTIARY = "#7676801F"  # 12% opacidad
    FILL_QUATERNARY = "#74748014"  # 8% opacidad

    # Rellenos modo oscuro
    FILL_DARK = "#7878805C"  # 36% opacidad
    FILL_SECONDARY_DARK = "#78788040"  # 25% opacidad
    FILL_TERTIARY_DARK = "#76768033"  # 20% opacidad
    FILL_QUATERNARY_DARK = "#74748024"  # 14% opacidad

    # ==================== COLORES DE FONDO ====================

    # Fondos modo claro
    BACKGROUND = "#FFFFFF"
    BACKGROUND_SECONDARY = "#F2F2F7"
    BACKGROUND_TERTIARY = "#FFFFFF"

    # Fondos modo oscuro
    BACKGROUND_DARK = "#000000"
    BACKGROUND_SECONDARY_DARK = "#1C1C1E"
    BACKGROUND_TERTIARY_DARK = "#2C2C2E"

    # Fondos agrupados modo claro
    GROUPED_BACKGROUND = "#F2F2F7"
    GROUPED_BACKGROUND_SECONDARY = "#FFFFFF"
    GROUPED_BACKGROUND_TERTIARY = "#F2F2F7"

    # Fondos agrupados modo oscuro
    GROUPED_BACKGROUND_DARK = "#000000"
    GROUPED_BACKGROUND_SECONDARY_DARK = "#1C1C1E"
    GROUPED_BACKGROUND_TERTIARY_DARK = "#2C2C2E"

    # ==================== COLORES DE SEPARADORES ====================

    SEPARATOR = "#3C3C434A"  # 29% opacidad
    SEPARATOR_OPAQUE = "#C6C6C8"

    SEPARATOR_DARK = "#545458"
    SEPARATOR_OPAQUE_DARK = "#38383A"

    # ==================== COLORES DE ENLACES ====================

    LINK = "#007AFF"
    LINK_DARK = "#0984FF"

    # ==================== COLORES ESPECIALES ====================

    # Placeholder text
    PLACEHOLDER = "#3C3C434D"  # 30% opacidad
    PLACEHOLDER_DARK = "#EBEBF54D"  # 30% opacidad

    # Fondo de selección
    SELECTION = "#007AFF33"  # 20% opacidad
    SELECTION_DARK = "#0A84FF33"  # 20% opacidad

    # ==================== COLORES SEMÁNTICOS ====================

    # Estados de éxito, advertencia, error
    SUCCESS = "#34C759"
    SUCCESS_DARK = "#30D158"

    WARNING = "#FF9500"
    WARNING_DARK = "#FF9F0A"

    ERROR = "#FF3B30"
    ERROR_DARK = "#FF453A"

    INFO = "#007AFF"
    INFO_DARK = "#0A84FF"

    # ==================== COLORES DE NAVEGACIÓN ====================

    # Barra de navegación
    NAV_BAR_BACKGROUND = "#F9F9F9"
    NAV_BAR_BACKGROUND_DARK = "#1C1C1E"

    # Toolbar
    TOOLBAR_BACKGROUND = "#F9F9F9"
    TOOLBAR_BACKGROUND_DARK = "#1C1C1E"

    # Tab bar
    TAB_BAR_BACKGROUND = "#F9F9F9"
    TAB_BAR_BACKGROUND_DARK = "#1C1C1E"

    TAB_BAR_SELECTED = "#007AFF"
    TAB_BAR_SELECTED_DARK = "#0A84FF"

    TAB_BAR_UNSELECTED = "#8E8E93"
    TAB_BAR_UNSELECTED_DARK = "#8E8E93"


# ==================== PALETAS TEMÁTICAS ====================


class LightTheme:
    """Tema claro completo"""

    PRIMARY = AppleColors.BLUE
    SECONDARY = AppleColors.GRAY
    SUCCESS = AppleColors.GREEN
    WARNING = AppleColors.ORANGE
    ERROR = AppleColors.RED
    INFO = AppleColors.TEAL

    TEXT = AppleColors.LABEL
    TEXT_SECONDARY = AppleColors.LABEL_SECONDARY
    TEXT_TERTIARY = AppleColors.LABEL_TERTIARY

    BACKGROUND = AppleColors.BACKGROUND
    BACKGROUND_SECONDARY = AppleColors.BACKGROUND_SECONDARY
    BACKGROUND_TERTIARY = AppleColors.BACKGROUND_TERTIARY

    BORDER = AppleColors.SEPARATOR
    BORDER_OPAQUE = AppleColors.SEPARATOR_OPAQUE


class DarkTheme:
    """Tema oscuro completo"""

    PRIMARY = AppleColors.BLUE_DARK
    SECONDARY = AppleColors.GRAY_DARK
    SUCCESS = AppleColors.GREEN_DARK
    WARNING = AppleColors.ORANGE_DARK
    ERROR = AppleColors.RED_DARK
    INFO = AppleColors.TEAL_DARK

    TEXT = AppleColors.LABEL_DARK
    TEXT_SECONDARY = AppleColors.LABEL_SECONDARY_DARK
    TEXT_TERTIARY = AppleColors.LABEL_TERTIARY_DARK

    BACKGROUND = AppleColors.BACKGROUND_DARK
    BACKGROUND_SECONDARY = AppleColors.BACKGROUND_SECONDARY_DARK
    BACKGROUND_TERTIARY = AppleColors.BACKGROUND_TERTIARY_DARK

    BORDER = AppleColors.SEPARATOR_DARK
    BORDER_OPAQUE = AppleColors.SEPARATOR_OPAQUE_DARK
