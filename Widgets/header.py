from styles import *
from Widgets.label import Label

class Header(Label):
    def __init__(self, text: str = '', length: int = 80) -> None:
        if not isinstance(length, int):
            raise TypeError(f'Expected int, got {type(length).__name__}')
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')

        super().__init__(text, length)

    
    def output(self) -> list:
        '''
        Returns the header as string inside of a list.
        '''
        return [str(self).strip()]


    def __str__(self) -> str:
        '''
        Returns the header as string.
        '''
        return TextStyles.ALL + super().__str__()