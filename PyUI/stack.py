from .pyui import PyUI

class Stack:
    def __init__(self) -> None:
        self.uis = []
        self.index = 0


    def add_ui(self, ui: PyUI) -> None:
        '''
        Adds `ui` to the Stacks UI's.
        '''
        if not isinstance(ui, PyUI):
            raise TypeError(f'Expected PyUI, got {type(ui).__name__}')

        self.uis.append(ui)


    def insert_ui(self, index: int, ui: PyUI) -> None:
        '''
        Inserts `ui` at position `index` to the Stacks UI's.
        '''
        if not isinstance(index, int):
            raise TypeError(f'Expected int, got {type(index).__name__}')
        if not isinstance(ui, PyUI):
            raise TypeError(f'Expected PyUI, got {type(ui).__name__}')

        self.uis.insert(index, ui)


    def remove_ui(self, ui: PyUI) -> None:
        '''
        Removes `ui` from the Stacks UI's.
        '''
        if not isinstance(ui, PyUI):
            raise TypeError(f'Expected PyUI, got {type(ui).__name__}')

        self.uis.remove(ui)


    def set_current_index(self, index: int) -> None:
        '''
        Sets the current UI to the UI at the position `index`.
        '''
        if index >= len(self.uis):
            raise IndexError(f'Expected index to be smaller than {len(self.uis)}, got {index}')
        if not isinstance(index, int):
            raise TypeError(f'Expected int, got {type(index).__name__}')

        self.index = index


    def get_current_index(self) -> int:
        '''
        Returns the index of the current UI.
        '''
        return self.index


    def get_current_ui(self) -> PyUI:
        '''
        Returns the UI at the current index.
        '''
        return self.uis[self.index]

    
    def get_uis(self) -> list:
        '''
        Returns a list of all UI's in the Stack.
        '''
        return self.uis


    def clear_uis(self) -> None:
        '''
        Removes all UI's from the Stack.
        '''
        self.uis = []


    def print(self) -> None:
        '''
        Calls the `.print()`-function on the current UI.
        '''
        self.uis[self.index].print()


    def __str__(self) -> str:
        '''
        Returns the current UI as a string.
        '''
        return str(self.uis[self.index])