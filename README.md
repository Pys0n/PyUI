# PyUI Documentation

## PyUI

To create a new PyUI use these lines of code:
```python
from pyui import PyUI

pyui = PyUI()
```

### .___str__() -> str
Returns the UI as multiline string.

This function allows you to use `str(pyui)` and `print(pyui)`.


### .add_widget(widget: ToggleSwitch | Label | Header | Button) -> None
Adds `widget` to the end of the UI.


### .clear_widgets() -> None
Removes all widgets from the UI.


### .get_size() -> tuple
Returns the current size of the UI as tuple (`(width, height)`).


### .get_widgets() -> list
Returns a list of all widgets in the order they are displayed.


### .interact_with_selected() -> bool | None
Interacts with `ToggleSwitch` and `Button` by calling `ToggleSwitch.toggle()` and `Button.press()` and returns what those function returns.


### .print() -> None
Prints the UI to the terminal.


### .select_next() -> ToggleSwitch | Label | Header | Button
Selects the next selectable widget in the UI and returns it.

To check if a widget is selectable or to change that, use `widget.selectable`.


### .select_previous() -> ToggleSwitch | Label | Header | Button
Selects the previous selectable widget in the UI and returns it.

To check if a widget is selectable or to change that, use `widget.selectable`.


### .set_background_color(background_color: BackgroundColor) -> None
Sets the background color of the UI to `background_color`.


### .update_size() -> tuple
Updates the UI's size to the terminal size and returns the new size as tuple (`(width, height)`).

## Widgets


### Button


### Header


### Label


### ToggleSwitch


## Styles


### BackgroundColor

There are currently four text colors:
- `BackgroundColor.BLACK`
- `BackgroundColor.BLUE`
- `BackgroundColor.GREEN`
- `BackgroundColor.RED`

With `BackgroundColor.RESET`, you can mark the end of an bold/italic/underlined paragraph.
**Attention:** `BackgroundColor.RESET` also resets `TextColor` and `TextStyle`


### TextColor

There are currently four text colors:
- `TextColor.BLUE`
- `TextColor.GRAY`
- `TextColor.GREEN`
- `TextColor.RED`

With `TextColor.RESET`, you can mark the end of an bold/italic/underlined paragraph.
**Attention:** `TextColor.RESET` also resets `BackgroundColor` and `TextStyle`


### TextStyle

There are currently three base styles:
- `TextStyle.BOLD` (**BOLD**)
- `TextStyle.ITALIC` (*ITALIC*)
- `TextStyle.UNDERLINE` (<u>UNDERLINE</u>)

and two combined styles:
- `TextStyle.BOLDITALIC` (***BOLDITALIC***)
- `TextStyle.ALL` (<u>***ALL***</u>)

With `TextStyle.RESET`, you can mark the end of an bold/italic/underlined paragraph.
**Attention:** `TextStyle.RESET` also resets `TextColor` and `BackgroundColor`
