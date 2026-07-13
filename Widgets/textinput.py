from styles import *

from Widgets.label import Label


def nothing(text):
    pass


class TextInput(Label):
    def __init__(self, text: str = '', length: int = 80) -> None:
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')
        if not isinstance(length, int):
            raise TypeError(f'Expected int, got {type(length).__name__}')

        super().__init__(text, length)

        self.on_change_do = nothing

    
    def add_text(self, text: str) -> str:
        '''
        Adds `text` to the text inputs current text.

        Calls the function set with `.on_change()`.

        Returns the new text.
        '''
        self.text += text

        self.on_change_do(self.text)

        return self.text


    def clear_text(self) -> None:
        '''
        Sets the text inputs text to `''`.

        Calls the function set with `.on_change()`.
        '''
        self.text = ''

        self.on_change_do(self.text)


    def remove_last(self) -> str:
        '''
        Removes the last element of the current text inputs text and returns it.

        Calls the function set with `.on_change()`.
        '''
        last = self.text[-1]
        self.text = self.text[:-1]

        self.on_change_do(self.text)

        return last


    def input(self, *args, **kwargs) -> str:
        '''
        Calls the `input()` function with the given `*args` and `**kwargs`.
        Sets the text inputs text to the entered text.

        Calls the function set with `.on_change()`.

        Returns the new text.
        '''
        self.text = input(*args, **kwargs)

        self.on_change_do(self.text)

        return self.text

    
    def on_change(self, function) -> None:
        '''
        Sets the function that gets called when using `.add_text()`, `.clear_text()`, `.input()` or `.remove_last()` to `function`.
        '''
        if not callable(function):
            raise TypeError(f'Expected function, got {type(function).__name__}')

        self.on_change_do = function


    def disconnect(self) -> None:
        '''
        Resets the function that gets called when using `.add_text()`, `.clear_text()`, `.input()` or `.remove_last()` to `function`.
        '''
        self.on_change_do = nothing


    def __str__(self) -> str:
        '''
        Returns the text input as a (multiline) string.
        '''
        string = ''
        for text in self.text.split('\n'):
            length = self.length - (self.spacer * 2 + 4)
            if len(text) > length:
                current_pos = 0
                parts = []
                while len(text) >= current_pos:
                    parts.append(text[current_pos:current_pos+length])
                    current_pos += length
                
                for part in parts:
                    string += (self.background_color if not self.selected else self.selected_color) + self.spacer * ' ' + self.text_color + '│ ' + part + self.spacer * ' ' + ' ' * (self.length - (len(part) + self.spacer * 2 + 4)) + ' │' + TextColor.RESET + '\n'
                
                continue

            string += (self.background_color if not self.selected else self.selected_color) + self.spacer * ' ' + self.text_color + '│ ' + text + self.spacer * ' ' + ' ' * (self.length - (len(text) + self.spacer * 2 + 4)) + ' │' + TextColor.RESET + '\n'

        return string
