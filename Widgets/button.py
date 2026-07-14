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
        '''
        Calls the function set with `.on_press()`.
        '''
        self.on_press_do()


    def on_press(self, function) -> None:
        '''
        Sets the function that gets called when using `.press()` to `function`.
        '''
        if not callable(function):
            raise TypeError(f'Expected function, got {type(function).__name__}')
        
        self.on_press_do = function


    def disconnect(self) -> None:
        '''

        Resets the function that gets called when using `.press()`.
        '''
        self.on_press_do = nothing

    
    def output(self) -> list:
        '''
        Returns the button as string inside of a list.
        '''
        return [str(self).strip()]


    def __str__(self) -> str:
        '''
        Returns the button as string.
        '''
        label = (self.background_color if not self.selected else self.selected_color) + self.indentation * ' ' + self.spacer * ' ' + self.text_color + '[ ' + self.text + ' ]' + self.spacer * ' ' + ' ' * (self.length - (len(self.text) + self.spacer * 2 + self.indentation + 4)) + TextColor.RESET

        return label