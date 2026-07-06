from styles import *
from Widgets.label import Label


def nothing():
    pass


class Button(Label):
    def __init__(self, text: str = '', length: int = 80) -> None:
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')
        if not isinstance(length, int):
            raise TypeError(f'Expected int, got {type(length).__name__}')

        super().__init__(text, length)

        self.on_press_do = nothing
        self.selectable = True

    
    def press(self) -> None:
        self.on_press_do()


    def on_press(self, function) -> None:
        if not callable(function):
            raise TypeError(f'Expected function, got {type(function).__name__}')
        
        self.on_press_do = function


    def disconnect(self) -> None:
        self.on_press_do = nothing

    
    def output(self) -> list:
        return [str(self).strip()]


    def __str__(self) -> str:
        label = (self.background_color if not self.selected else self.selected_color) + self.spacer * ' ' + self.text_color + '[ ' + self.text + ' ]' + self.spacer * ' ' + ' ' * (self.length - (len(self.text) + self.spacer * 2 + 4)) + TextColor.RESET

        return label