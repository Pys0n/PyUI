import os

from styles import *
from widgets import *

class PyUI:
    def __init__(self) -> None:
        self.background_color = BackgroundColor.BLACK

        self.widgets = []
        self.widget_spacer = 1
        self.spacer = 5

        size = os.get_terminal_size()
        self.height = size.lines
        self.width = size.columns

        self.scroll_status = -1
        self.selected = 0

    
    def set_background_color(self, background_color: BackgroundColor) -> None:
        '''
        Sets the background color of the UI to `background_color`.
        '''
        if not isinstance(background_color, str):
            raise TypeError(f'Expected BackgroundColor, got {type(background_color).__name__}')
    
        self.background_color = background_color


    def clear_widgets(self) -> None:
        '''
        Removes all widgets from the UI.
        '''
        self.widgets = []

    
    def add_widget(self, widget: ToggleSwitch | Label | Header | Button | TextInput | Expandable) -> None:
        '''
        Adds `widget` to the end of the UI.
        '''
        if not isinstance(widget, ToggleSwitch) and not isinstance(widget, Label) and not isinstance(widget, Header) and not isinstance(widget, Button) and not isinstance(widget, TextInput) and not isinstance(widget, Expandable):
            raise TypeError(f'Expected ToggleSwitch, Label, Header, Button, TextInput or Expandable, got {type(widget).__name__}')

        self.widgets.append(widget)

        if self.widgets[self.selected] == widget:
            if widget.selectable:
                widget.selected = True
            else:
                self.selected += 1


    def insert_widget(self, index: int, widget: ToggleSwitch | Label | Header | Button | TextInput | Expandable) -> None:
        '''
        Inserts `widget` at `index` to the UI's widgets.
        '''
        if not isinstance(widget, ToggleSwitch) and not isinstance(widget, Label) and not isinstance(widget, Header) and not isinstance(widget, Button) and not isinstance(widget, TextInput) and not isinstance(widget, Expandable):
            raise TypeError(f'Expected ToggleSwitch, Label, Header, Button, TextInput or Expandable, got {type(widget).__name__}')
        if not isinstance(index, int):
            raise TypeError(f'Expected int, got {type(index).__name__}')

        self.widgets.insert(index, widget)

        if self.widgets[self.selected] == widget:
            if widget.selectable:
                widget.selected = True
            else:
                self.selected += 1

    
    def remove_widget(self, widget: ToggleSwitch | Label | Header | Button | TextInput | Expandable) -> None:
        '''
        Removes `widget` from the UI's widgets.
        '''
        if widget not in self.widgets:
            raise ValueError(f'Widget not in widgets.')

        if self.widgets[self.selected] == widget:
            found = False
            for i, nwidget in enumerate(self.widgets[self.widgets.index(widget)+1:]):
                if nwidget.selectable:
                    self.selected = self.widgets.index(widget) + i + 1
                    nwidget.selected = True
                    found = True
                    break

            if not found:
                for i in range(self.widgets.index(widget)):
                    if self.widgets[self.widgets.index(widget) - (i + 1)].selectable:
                        self.selected = self.widgets.index(widget) - (i + 1)
                        self.widgets[self.widgets.index(widget) - (i + 1)].selected = True
                        found = True
                        break
            
            if not found:
                self.selected = 0

        self.widgets.remove(widget)

    
    def get_widgets(self) -> list:
        '''
        Returns a list of all widgets in the order they are displayed.
        '''
        return self.widgets

    
    def select_next(self) -> ToggleSwitch | Label | Header | Button | TextInput | Expandable:
        '''
        Selects the next selectable widget in the UI and returns it.

        To check if a widget is selectable or to change that, use `widget.selectable`.
        '''
        previous = self.widgets[self.selected]
        for increasment, item in enumerate(self.widgets[self.selected+1:]):
            if item.selectable:
                self.selected += increasment + 1
                self.scroll_status += increasment + 1
                item.selected = True
                previous.selected = False
                return item


    def get_size(self) -> tuple:
        '''
        Returns the current size of the UI as tuple (`(width, height)`).
        '''
        return (self.width, self.height)

    
    def update_size(self) -> tuple:
        '''
        Updates the UI's size to the terminal size and returns the new size as tuple (`(width, height)`).
        '''
        size = os.get_terminal_size()
        self.height, self.width = size.lines, size.columns

        return (self.width, self.height)


    def select_previous(self) -> ToggleSwitch | Label | Header | Button | TextInput | Expandable:
        '''
        Selects the previous selectable widget in the UI and returns it.

        To check if a widget is selectable or to change that, use `widget.selectable`.
        '''
        previous = self.widgets[self.selected]
        for decreasment, item in enumerate(self.widgets[:self.selected][::-1]):
            if item.selectable:
                self.selected -= decreasment + 1
                self.scroll_status -= decreasment + 1
                item.selected = True
                previous.selected = False
                return item

    
    def interact_with_selected(self) -> bool | None:
        '''
        Interacts with `ToggleSwitch` and `Button` by calling `ToggleSwitch.toggle()` and `Button.press()` and returns what those function returns.
        '''
        widget = self.widgets[self.selected]

        if isinstance(widget, ToggleSwitch):
            return widget.toggle()

        if isinstance(widget, Button):
            return widget.press()

        if isinstance(widget, Expandable):
            return widget.toggle()


    def print(self) -> None:
        '''
        Prints the UI to the terminal.
        '''
        print(self)

    
    def __str__(self) -> str:
        '''
        Returns the UI as multiline string.
        '''
        screen = []
        size = os.get_terminal_size()
        self.height, self.width = size.lines, size.columns

        line_index = 0
        while len(self.widgets) * (self.widget_spacer + 1) > line_index or len(screen) < self.height:
            index = (1 / (self.widget_spacer + 1)) * (line_index+1)
            if len(self.widgets) <= int(index)-1 or index != int(index):
                line = ''
                for _ in range(self.width):
                    line += self.background_color + ' ' + BackgroundColor.RESET
                screen.append(line)
            else:
                if self.widgets[int(index)-1].is_hidden():
                    for _ in range(self.widget_spacer):
                        if len(screen) > 0: screen.pop(-1)
                    
                    line_index += 1
                    continue

                widget_strs = self.widgets[int(index)-1].output()
                for widget_str in widget_strs:
                    screen.append(self.background_color + self.spacer * ' ' + widget_str + self.background_color + ' ' * (self.width - (self.widgets[int(index)-1].length + 2 * self.spacer)) + self.spacer * ' ' + BackgroundColor.RESET)
        
            line_index += 1

        screen_min = max(min(self.scroll_status*(self.widget_spacer+1), len(screen)-self.height), 0)
        screen_max = max(min(self.height+self.scroll_status*(self.widget_spacer+1), len(screen)), self.height)
        return ''.join(screen[screen_min:screen_max-1])


    def __len__(self) -> int:
        '''
        Returns the number of widgets in the UI.
        '''
        return len(self.widgets)