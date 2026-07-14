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
        Returns the header switch splited at newlines as list.
        '''
        return [(TextStyles.BOLDITALIC if i != len(str(self).strip().split('\n'))-1 else TextStyles.ALL) + x for i, x in enumerate(str(self).strip().split('\n'))]


    def __str__(self) -> str:
        '''
        Returns the header as a (multiline) string.
        '''
        return super().__str__()