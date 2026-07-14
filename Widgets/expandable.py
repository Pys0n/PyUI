from styles import *

from Widgets.button import Button
from Widgets.header import Header
from Widgets.label import Label
from Widgets.textinput import TextInput
from Widgets.toggle_switch import ToggleSwitch


def nothing(expanded):
    pass


class Expandable(Label):
    def __init__(self, parent, text: str = '', length: int = 80) -> None:
        if not isinstance(length, int):
            raise TypeError(f'Expected int, got {type(length).__name__}')
        if not isinstance(text, str):
            raise TypeError(f'Expected str, got {type(text).__name__}')

        super().__init__(text, length)

        self.parent = parent

        self.widgets = []

        self.expanded = False
        self.selectable = True

        self.text_spacer = 2

        self.on_toggle_do = nothing


    def set_text_spacer(self, text_spacer: int) -> None:
        '''
        Sets the number of spaces between the current states indicator (`>` or `v`) and the text.
        '''
        if not isinstance(text_spacer, int):
            raise TypeError(f'Expected int, got {type(text_spacer).__name__}')

        self.text_spacer = text_spacer

    
    def get_text_spacer(self) -> int:
        '''
        Returns the number of spaces between the current states indicator (`>` or `v`) and the text.
        '''
        return self.text_spacer


    def expand(self) -> None:
        '''
        Expands the widget (all sub-widgets are going to be visible).

        Calls the function set with `.on_toggle()`.
        '''
        self.expanded = True

        for widget in self.widgets:
            widget.show()

        self.on_toggle_do(True)

    
    def collapse(self) -> None:
        '''
        Collapses the widget (all sub-widgets are going to be hidden).

        Calls the function set with `.on_toggle()`.
        '''
        self.expanded = False

        for widget in self.widgets:
            widget.hide()

        self.on_toggle_do(False)

    
    def toggle(self) -> bool:
        '''
        Expands the widget if it is collapsed and collapses the widget if it is expanded.

        Returns `True` if the widget got expanded and `False` if the widget got collpased.

        Calls the function set with `.on_toggle()`.
        '''
        if self.expanded:
            self.collapse()
        else:
            self.expand()

        return self.is_expanded()


    def on_toggle(self, function) -> None:
        '''
        Sets the function that gets called when using `.expand()`, `.collapse()` or `.toggle()` to `function`.
        '''
        if not callable(function):
            raise TypeError(f'Expected function, got {type(function).__name__}')

        self.on_toggle_do = function


    def disconnect(self) -> None:
        '''
        Resets the function that gets called when using `.expand()`, `.collapse()` or `.toggle()`.
        '''
        self.on_toggle_do = nothing


    def is_expanded(self) -> bool:
        '''
        Returns `True` if the widget is expanded and `False` if the widget is collapsed.
        '''
        return self.expanded


    def clear_widgets(self) -> None:
        '''
        Removes all widgets from the expandable.
        '''
        for widget in self.widgets[:]:
            self.remove_widget(widget)

    
    def add_widget(self, widget: ToggleSwitch | Label | Header | Button | TextInput) -> None:
        '''
        Adds `widget` to the end of the expandable.
        '''
        if not isinstance(widget, ToggleSwitch) and not isinstance(widget, Label) and not isinstance(widget, Header) and not isinstance(widget, Button) and not isinstance(widget, TextInput) and not isinstance(widget, Expandable):
            raise TypeError(f'Expected ToggleSwitch, Label, Header, Button, TextInput or Expandable, got {type(widget).__name__}')
        if self not in self.parent.widgets:
            raise ValueError(f'Expandable isn\'t a widget of an PyUI or another Expandable yet!')

        if not self.expanded: widget.hide()
        widget.indentation = self.indentation + 2

        self.widgets.append(widget)

        index = self.parent.widgets.index(self)
        self.parent.insert_widget(index+self.widgets.index(widget)+1, widget)


    def insert_widget(self, index: int, widget: ToggleSwitch | Label | Header | Button | TextInput) -> None:
        '''
        Inserts `widget` at `index` to the expandable's widgets.
        '''
        if not isinstance(widget, ToggleSwitch) and not isinstance(widget, Label) and not isinstance(widget, Header) and not isinstance(widget, Button) and not isinstance(widget, TextInput) and not isinstance(widget, Expandable):
            raise TypeError(f'Expected ToggleSwitch, Label, Header, Button, TextInput or Expandable, got {type(widget).__name__}')
        if not isinstance(index, int):
            raise TypeError(f'Expected int, got {type(index).__name__}')
        if self not in self.parent.widgets:
            raise ValueError(f'Expandable isn\'t a widget of an PyUI or another Expandable yet!')

        if not self.expanded: widget.hide()
        widget.indentation = self.indentation + 2

        self.widgets.insert(index, widget)

        index = self.parent.widgets.index(self)
        self.parent.insert_widget(index+self.widgets.index(widget)+1, widget)

    
    def remove_widget(self, widget: ToggleSwitch | Label | Header | Button | TextInput) -> None:
        '''
        Removes `widget` from the expandable's widgets.
        '''
        
        self.parent.remove_widget(widget)
        widget.indentation -= 2
        widget.show()


    def get_widgets(self) -> list:
        '''
        Returns a list of all widgets in the order they are displayed.
        '''
        return self.widgets


    def output(self) -> list:
        '''
        Returns the expandable as string inside of a list.
        '''
        return [str(self).strip()]


    def __str__(self) -> str:
        '''
        Returns the expandable as a string.
        '''
        if self.expanded:
            expandable = (self.background_color if not self.selected else self.selected_color) + self.indentation * ' ' + self.spacer * ' ' + self.text_color + 'v' + self.text_spacer * ' ' + self.text + self.spacer * ' ' + TextColor.RESET
        else:
            expandable = (self.background_color if not self.selected else self.selected_color) + self.indentation * ' ' + self.spacer * ' ' + self.text_color + '>' + self.text_spacer * ' ' + self.text + self.spacer * ' ' + TextColor.RESET
        
        expandable += (self.background_color if not self.selected else self.selected_color) + ' ' * (self.length - (len(self.text) + self.spacer * 2 + self.text_spacer + self.indentation + 1)) + BackgroundColor.RESET

        return expandable


    def __len__(self) -> int:
        '''
        Returns the number of widgets inside the expandable.
        '''
        return len(self.widgets)