# PyUI Documentation

- [PyUI](#pyui)
- [Widgets](#widgets)
    - [Button](#button)
    - [Header](#header)
    - [Label](#label)
    - [TextInput](#textinput)
    - [ToggleSwitch](#toggleswitch)
- [Styles](#styles)
    - [BackgroundColor](#backgroundcolor)
    - [TextColor](#textcolor)
    - [TextStyle](#textstyle)


## PyUI

To create a new PyUI use these lines of code:
```python
from pyui import PyUI

pyui = PyUI()
```


### .\_\_len\_\_() -> int
Returns the number of widgets in the UI.

This function allows you to use `len(pyui)` to get the count of widgets in it.


### .\_\_str\_\_() -> str
Returns the UI as multiline string.

This function allows you to use `str(pyui)` and `print(pyui)`.


### .add_widget(widget: ToggleSwitch | Label | Header | Button | TextInput) -> None
Adds `widget` to the end of the UI.


### .clear_widgets() -> None
Removes all widgets from the UI.


### .get_size() -> tuple
Returns the current size of the UI as tuple (`(width, height)`).


### .get_widgets() -> list
Returns a list of all widgets in the order they are displayed.


### .insert_widget(index: int, widget: ToggleSwitch | Label | Header | Button | TextInput) -> None
Inserts `widget` at `index` to the UI's widgets.


### .interact_with_selected() -> bool | None
Interacts with `ToggleSwitch` and `Button` by calling `ToggleSwitch.toggle()` and `Button.press()` and returns what those function returns.


### .print() -> None
Prints the UI to the terminal.


### .select_next() -> ToggleSwitch | Label | Header | Button | TextInput
Selects the next selectable widget in the UI and returns it.

To check if a widget is selectable or to change that, use `widget.selectable`.


### .select_previous() -> ToggleSwitch | Label | Header | Button | TextInput
Selects the previous selectable widget in the UI and returns it.

To check if a widget is selectable or to change that, use `widget.selectable`.


### .set_background_color(background_color: BackgroundColor) -> None
Sets the background color of the UI to `background_color`.


### .update_size() -> tuple
Updates the UI's size to the terminal size and returns the new size as tuple (`(width, height)`).

## Widgets


### Button

To create a new Button use these lines of code:
```python
from widgets import Button

button = Button()
```

Optionally, you can give the Button a text and a length when creating:
```python
button = Button('Text', 100)
```

The default text is `''` and the default length is `80`.


`Button` inherits *all* functions from `Label`, except `.output()` and `.__str__()` and has three unqiue functions: `.press()`, `.on_press()` and `.disconnect()`.


#### .\_\_str\_\_() -> str
Returns the button as string.


#### .disconnect() -> None
Resets the function that gets called when using `.press()`.

The function by default does nothing.


#### .on_press(function) -> None
Sets the function that gets called when using `.press()` to `function`.

The function by default does nothing.


#### .output() -> list
Returns the button as string inside of a list.

**Buttons are not allowed to be multiline Buttons!**


#### .press() -> None
Calls the function set with `.on_press()`.

The function by default does nothing.


### Header

To create a new Header use these lines of code:
```python
from widgets import Header

header = Header()
```

Optionally, you can give the Header a text and a length when creating:
```python
header = Header('Text', 100)
```

The default text is `''` and the default length is `80`.


`Header` inherits *all* functions from `Label`, except `.output()` and `.__str__()`.


#### .\_\_str\_\_() -> str
Returns the header as string.


#### .output() -> list
Returns the header as string inside of a list.

**Headers are not allowed to be multiline Headers!**


### Label

To create a new Label use these lines of code:
```python
from widgets import Label

label = Label()
```

Optionally, you can give the label a text and a length when creating:
```python
label = Label('Text', 100)
```

The default text is `''` and the default length is `80`.


#### .\_\_str\_\_() -> str
Returns the label as a (multiline) string.


#### .get_select() -> bool
Returns `True` if the label is selected.
This can be set by using `.set_select()`.


#### .get_selectable() -> bool
Returns `True` if the label is selectable.
This can be set by using `.set_selectable()`.


#### .get_spacer() -> int
Returns the number of spaces before and after the widgets main content.
This can be set by using `.set_spacer()`.


#### .get_text() -> str
Returns the current text of the label.


#### .hide() -> None
Sets the `hidden` attribute to `True`.

If a widget is hidden it won't be displayed when using `.print()` on your PyUI.


#### .is_hidden() -> bool
Returns the current value of the `hidden` attribute.

The `hidden` attribute can be changed by calling `.show()` or `.hide()`.


#### .output() -> list
Returns the label splited at newlines as list.


#### .set_background_color(background_color: BackgroundColor) -> None
Sets the background color of the label.


#### .set_select(select: bool) -> None
If `select` equals `True`, use the selected color instead of the background color as background color.


#### .set_selectable(selectable: bool) -> None
If `selectable` equals `False`, the PyUI of this label is not going to select it and instead skips it.

A label is by default not selectable.


#### .set_selected_color(selected_color: BackgroundColor) -> None
Sets the background color when selected / hovered.


#### .set_spacer(spacer: int) -> None
Sets the number of spaces before and after the widgets main content.


#### .set_text_color(text_color: TextColor) -> None
Sets the color of the labels text.


#### .set_text(text: str) -> None
Sets the labels text to the value of `text`.

If the text contains newlines (`\n`) the label will be a multiline label.


#### .show() -> None
Sets the `hidden` attribute to `False`.

If a widget is hidden it won't be displayed when using `.print()` on your PyUI.



### TextInput

To create a new TextInput use these lines of code:
```python
from widgets import TextInput

text_input = TextInput()
```

Optionally, you can give the TextInput a text and a length when creating:
```python
text_input = TextInput('Text', 100)
```

The default text is `''` and the default length is `80`.


`TextInput` inherits *all* functions from `Label`, except `.__str__()` and has two unqiue functions: `.add_text()`, `.clear_text()` and `.input()`.


#### .\_\_str\_\_() -> str
Returns the text input as a (multiline) string.


#### .add_text(text: str) -> str
Adds `text` to the text inputs current text.

Returns the new text.


#### .clear_text() -> None
Sets the text inputs text to `''`.


#### .input(*args, **kwargs) -> str
Calls the `input()` function with the given `*args` and `**kwargs`.
Sets the text inputs text to the entered text.

Returns the new text.


#### .remove_last() -> str
Removes the last element of the current text inputs text and returns it.



### ToggleSwitch

To create a new ToggleSwitch use these lines of code:
```python
from widgets import ToggleSwitch

toggle_switch = ToggleSwitch()
```

Optionally, you can give the ToggleSwitch a text and a length when creating:
```python
toggle_switch = ToggleSwitch('Text', 100)
```

The default text is `''` and the default length is `80`.


`ToggleSwitch` inherits *all* functions from `Label`, except `.output()` and `.__str__()` and has 8 unqiue functions.


#### .\_\_str\_\_() -> str
Returns the toggle switch as string.


#### .disconnect() -> None
Resets the function that gets called when using `.toggle()` to `function`.

The function by default does nothing.


#### .get_text_spacer() -> int
Returns the size of the spacer between the toggle switch and the text. 


#### .on_toggle(function) -> None
Sets the function that gets called when using `.toggle()` to `function`.

The function by default does nothing.


#### .output() -> list
Returns the toggle switch as string inside of a list.

**ToggleSwitches are not allowed to be multiline ToggleSwitches!**


#### .set_off_color(off_color: TextColor) -> None
Sets the color of the toggle switch to `off_color` when the current state equals off.


#### .set_on_color(on_color: TextColor) -> None
Sets the color of the toggle switch to `on_color` when the current state equals on.


#### .set_text_spacer(text_spacer: int) -> None
Sets the size of the spacer between the toggle switch and the text. 


#### .set_track_color(track_color: TextColor) -> None
Sets the color of the toggle switch track to `track_color`.


#### .toggle() -> bool
If the current state of the toggle switch is on, set the state to off and return `False` (the new state).
If the current state of the toggle switch is off, set the state to on and return `True` (the new state).

Calls the function set with `.on_toggle()`.


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
