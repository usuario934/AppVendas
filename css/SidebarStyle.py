import flet as ft

container_sidebar: dict = {
    "bgcolor": "#3C4350",
    "padding": 4,
    "width": 220,
    "clip_behavior": ft.ClipBehavior.ANTI_ALIAS,
    "animate": ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT)
}

container_sidebar2: dict = {
    "spacing": 0,
}

menu = {
    "width": 220,
    "bgcolor": "#3C4350",
    "padding": 4,
    "animate": ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT)
}

content_sidebar = {
    "width": 0,
    "bgcolor": "#333945",
    "padding": 5,
    "animate": ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
}