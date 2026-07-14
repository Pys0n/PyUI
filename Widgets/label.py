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
        self.hidden = False

        self.text = text
        self.spacer = 2
        self.indentation = 0

        self.length = length


    def set_background_color(self, background_color: BackgroundColor) -> None:
        '''
        Sets the background color of the label.
        '''
        if not isinstance(background_color, str):
            raise TypeError(f'Expected BackgroundColor, got {type(background_color).__name__}')
    
        self.background_color = background_color


    def set_selected_color(self, selected_color: BackgroundColor) -> None:
        '''
        Sets the background color when selected / hovered.
        '''
        if not isinstance(selected_color, str):
            raise TypeError(f'Expected BackgroundColor, got {type(selected_color).__name__}')
    
        self.selected_color = selected_color


    def set_text_color(self, text_color: TextColor) -> None:
        '''
        Sets the color of the labels text.
        '''
        if not isinstance(text_color, str):
            raise TypeError(f'Expected TextColor, got {type(text_color).__name__}')
    
        self.text_color = text_color

    
    def set_text(self, text: str) -> None:
        '''
        Sets the labels text to the value of `text`.
        '''
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')
        
        self.text = text

    
    def get_text(self) -> str:
        '''
        Returns the current text of the label.
        '''
        return self.text


    def set_select(self, select: bool) -> None:
        '''
        If `select` equals `True`, use the selected color instead of the background color as background color.
        '''
        if not isinstance(select, bool):
            raise TypeError(f'Expected bool, got {type(select).__name__}')
        self.selected = select


    def get_select(self) -> bool:
        '''
        Returns `True` if the label is selected.
        This can be set by using `.set_select()`.
        '''
        return self.selected

    
    def set_selectable(self, selectable: bool) -> None:
        '''
        If `selectable` equals `False`, the PyUI of this label is not going to select it and instead skips it.

        A label is by default not selectable.
        '''
        if not isinstance(selectable, bool):
            raise TypeError(f'Expected bool, got {type(selectable).__name__}')

        self.selectable = selectable

    
    def get_selectable(self) -> bool:
        '''
        Returns `True` if the label is selectable.
        This can be set by using `.set_selectable()`.
        '''
        return self.selectable

    
    def set_spacer(self, spacer: int) -> None:
        '''
        Sets the number of spaces before and after the widgets main content.
        '''
        if not isinstance(spacer, int):
            raise TypeError(f'Expected int, got {type(spacer).__name__}')
        if spacer < 0:
            raise ValueError(f'Expected spacer to be greater then zero, got {spacer}')

        self.spacer = spacer

    
    def get_spacer(self) -> int:
        '''
        Returns the number of spaces before and after the widgets main content.
        This can be set by using `.set_spacer()`.
        '''
        return self.spacer


    def show(self) -> None:
        '''
        Sets the `hidden` attribute to `False`.

        If a widget is hidden it won't be displayed when using `.print()` on your PyUI.
        '''
        self.hidden = False


    def hide(self) -> None:
        '''
        Sets the `hidden` attribute to `True`.

        If a widget is hidden it won't be displayed when using `.print()` on your PyUI.
        '''
        self.hidden = True


    def is_hidden(self) -> bool:
        '''
        Returns the current value of the `hidden` attribute.
        '''
        return self.hidden

    
    def output(self) -> list:
        '''
        Returns the label splited at newlines as list.
        '''
        return str(self).strip().split('\n')


    def __str__(self) -> str:
        '''
        Returns the label as a (multiline) string.
        '''
        string = ''
        for text in self.text.split('\n'):
            length = self.length - (self.spacer * 2)
            if len(text) > length:
                current_pos = 0
                parts = []
                while len(text) >= current_pos:
                    parts.append(text[current_pos:current_pos+length])
                    current_pos += length
                
                for part in parts:
                    string += (self.background_color if not self.selected else self.selected_color) + self.indentation * ' ' + self.spacer * ' ' + self.text_color + part + self.spacer * ' ' + ' ' * (self.length - (len(part) + self.spacer * 2 + self.indentation)) + TextColor.RESET + '\n'
                
                continue

            string += (self.background_color if not self.selected else self.selected_color) + self.indentation * ' ' + self.spacer * ' ' + self.text_color + text + self.spacer * ' ' + ' ' * (self.length - (len(text) + self.spacer * 2 + self.indentation)) + TextColor.RESET + '\n'

        return string