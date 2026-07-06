from styles import *

class Label:
    def __init__(self, text: str = '', length: int = 80) -> None:
        if not isinstance(length, int):
            raise TypeError(f'Expected int, got {type(length).__name__}')
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')

        self.background_color = BackgroundColor.BLACK
        self.selected_color = BackgroundColor.GREEN
        self.text_color = TextColor.GRAY

        self.selected = False
        self.selectable = False

        self.text = text
        self.spacer = 2

        self.length = length


    def set_background_color(self, background_color: BackgroundColor) -> None:
        if not isinstance(background_color, str):
            raise TypeError(f'Expected BackgroundColor, got {type(background_color).__name__}')
    
        self.background_color = background_color


    def set_selected_color(self, selected_color: BackgroundColor) -> None:
        if not isinstance(selected_color, str):
            raise TypeError(f'Expected BackgroundColor, got {type(selected_color).__name__}')
    
        self.selected_color = selected_color


    def set_text_color(self, text_color: TextColor) -> None:
        if not isinstance(text_color, str):
            raise TypeError(f'Expected TextColor, got {type(text_color).__name__}')
    
        self.text_color = text_color

    
    def set_text(self, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')
        
        self.text = text

    
    def get_text(self) -> str:
        return self.text


    def set_select(self, select: bool) -> None:
        if not isinstance(select, bool):
            raise TypeError(f'Expected bool, got {type(select).__name__}')
        self.selected = select


    def get_select(self) -> bool:
        return self.selected

    
    def set_selectable(self, selectable: bool) -> None:
        if not isinstance(selectable, bool):
            raise TypeError(f'Expected bool, got {type(selectable).__name__}')

        self.selectable = selectable

    
    def get_selectable(self) -> bool:
        return self.selectable

    
    def set_spacer(self, spacer: int) -> None:
        if not isinstance(spacer, int):
            raise TypeError(f'Expected int, got {type(spacer).__name__}')
        if spacer < 0:
            raise ValueError(f'Expected spacer to be greater then zero, got {spacer}')

        self.spacer = spacer

    
    def get_spacer(self) -> int:
        return self.spacer

    
    def output(self) -> list:
        return str(self).strip().split('\n')


    def __str__(self) -> str:
        string = ''
        for text in self.text.split('\n'):
            string += (self.background_color if not self.selected else self.selected_color) + self.spacer * ' ' + self.text_color + text + self.spacer * ' ' + ' ' * (self.length - (len(text) + self.spacer * 2)) + TextColor.RESET + '\n'

        return string