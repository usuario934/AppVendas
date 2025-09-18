import flet as ft


container_menu: dict = {
    "expand": True,
    "height": 50,
    "bgcolor": "#515B6E"
}

container_search: dict = {
    "bgcolor": "white",
    "border_radius": ft.border_radius.all(4),
    "border": ft.border.all(2, "#cccccc"),
    "padding": ft.padding.symmetric(0, 5)
}

container_person: dict = {
    "bgcolor": "#515B6E",
    "border_radius": 50,
    "border": ft.border.all(2, "#3C4350"),
    "padding": ft.padding.symmetric(5, 8)
}


container_menu_top: dict = {
    "bgcolor": "white",
    "height": 32,
    "alignment": ft.alignment.center_left,
    "padding": ft.padding.symmetric(4, 10),
    "border": ft.border.only(bottom=ft.BorderSide(2, color="#cccccc"))
}


container_menu_bottom: dict = {
    "expand": 1,
    "bgcolor": "white",
    "padding": ft.padding.symmetric(4, 10),
    "border": ft.border.only(top=ft.BorderSide(2, color="#cccccc"))
}