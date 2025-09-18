import flet as ft

button_menu: dict = {
    "shape": ft.RoundedRectangleBorder(radius=4),
    "color": "white",
    "alignment": ft.alignment.center_left,
    "icon_size": 25
}

button_content: dict = {
    "shape": ft.RoundedRectangleBorder(radius=4),
    "color": "white",
    "alignment": ft.alignment.center_left
}

button_search_icon: dict = {
    "icon": ft.Icons.SEARCH_ROUNDED,
    "icon_size": 18,
    "icon_color": "#cccccc",
    "hover_color": "transparent",
    "padding": 0
}

button_person_icon: dict = {
    "icon": ft.Icons.PERSON,
    "icon_size": 28,
    "icon_color": "orange",
    "bgcolor": "white",
    "alignment": ft.alignment.center,
    "padding": ft.padding.all(0)
}