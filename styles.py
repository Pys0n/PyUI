class BackgroundColor:
    DEFAULT = ''
    BLACK = '\033[48;2;0;0;0m'
    BLUE = '\033[48;2;0;0;50m'
    GREEN = '\033[48;2;0;50;0m'
    RED = '\033[48;2;50;0;0m'
    RESET = '\033[0m'


class TextColor:
    DEFAULT = ''
    BLUE = '\033[38;2;0;0;150m'
    GRAY = '\033[38;2;200;200;200m'
    GREEN = '\033[38;2;0;150;0m'
    RED = '\033[38;2;150;0;0m'
    RESET = '\033[0m'


class TextStyles:
    DEFAULT = ''
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BOLDITALIC = '\033[1;3m'
    ALL = '\033[1;3;4m'
    RESET = '\033[0m'


class TextInputMode:
    DEFAULT = 0
    PASSWORD = 1
