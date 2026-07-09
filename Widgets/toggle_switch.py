import os

from styles import *
from Widgets.label import Label

def nothing(toggle):
    pass

class ToggleSwitch(Label):
    def __init__(self, text: str = '', length: int = 80, default_state: bool = True) -> None:
        if not isinstance(default_state, bool):
            raise TypeError(f'Expected bool, got {type(default_state).__name__}')
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')
        if not isinstance(length, int):
            raise TypeError(f'Expected int, got {type(length).__name__}')

        super().__init__(text, length)

        self.on_color = TextColor.GREEN
        self.off_color = TextColor.GRAY
        self.track_color = TextColor.GRAY

        self.state = default_state
        self.default_state = default_state
        self.on_toggle_do = nothing
        self.selectable = True

        self.text_spacer = 2


    def set_on_color(self, on_color: TextColor) -> None:
        '''
        Sets the color of the toggle switch to `on_color` when the current state equals on.
        '''
        if not isinstance(on_color, str):
            raise TypeError(f'Expected TextColor, got {type(on_color).__name__}')
    
        self.on_color = on_color


    def set_off_color(self, off_color: TextColor) -> None:
        '''
        Sets the color of the toggle switch to `off_color` when the current state equals off.
        '''
        if not isinstance(off_color, str):
            raise TypeError(f'Expected TextColor, got {type(off_color).__name__}')
    
        self.off_color = off_color


    def set_track_color(self, track_color: TextColor) -> None:
        '''
        Sets the color of the toggle switch track to `track_color`.
        '''
        if not isinstance(track_color, str):
            raise TypeError(f'Expected TextColor, got {type(track_color).__name__}')
    
        self.track_color = track_color

    
    def toggle(self) -> bool:
        '''
        If the current state of the toggle switch is on, set the state to off and return `False` (the new state).
        If the current state of the toggle switch is off, set the state to on and return `True` (the new state).
        
        Calls the function set with `.on_toggle()`.
        '''
        self.state = not self.state
        
        self.on_toggle_do(self.state)

        return self.state
    

    def on_toggle(self, function) -> None:
        '''
        Sets the function that gets called when using `.toggle()` to `function`.
        '''
        if not callable(function):
            raise TypeError(f'Expected function, got {type(function).__name__}')

        self.on_toggle_do = function

    
    def disconnect(self) -> None:
        '''
        Resets the function that gets called when using `.toggle()` to `function`.
        '''
        self.on_toggle_do = nothing

    
    def set_text_spacer(self, text_spacer: int) -> None:
        '''
        Sets the size of the spacer between the toggle switch and the text. 
        '''
        if not isinstance(text_spacer, int):
            raise TypeError(f'Expected int, got {type(text_spacer).__name__}')
        if text_spacer < 0:
            raise ValueError(f'Expected text_spacer to be greater then zero, got {text_spacer}')

        self.text_spacer = text_spacer

    
    def get_text_spacer(self) -> int:
        '''
        Returns the size of the spacer between the toggle switch and the text. 
        '''
        return self.text_spacer

    
    def output(self) -> list:
        '''
        Returns the toggle switch as string inside of a list.
        '''
        return [str(self).strip()]


    def __str__(self) -> str:
        '''
        Returns the toggle switch as string.
        '''
        if self.state:
            toggleswitch = (self.background_color if not self.selected else self.selected_color) + self.spacer * ' ' + self.track_color + '━' + self.on_color + '█' + self.text_spacer * ' ' + self.text_color + self.text + self.spacer * ' ' + TextColor.RESET
        else:
            toggleswitch = (self.background_color if not self.selected else self.selected_color) + self.spacer * ' ' + self.off_color + '█' + self.track_color + '━' + self.text_spacer * ' ' + self.text_color + self.text + self.spacer * ' ' + TextColor.RESET
        
        toggleswitch += (self.background_color if not self.selected else self.selected_color) + ' ' * (self.length - (len(self.text) + self.spacer * 2 + self.text_spacer + 2)) + BackgroundColor.RESET

        return toggleswitch