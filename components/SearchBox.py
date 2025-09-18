import flet as ft
from AppDesktop.css import MenuStyle, ButtonStyle, TextField

class Search(ft.Container):
    def __init__(self,
                 width: int = 200,
                 heigth: int = 40,
                 font_size: int | float = 12):
        super().__init__()

        # --------------------------------------------------------------------------------------------------------------
        #
        # Atribuição das variaveis de customização do container.
        #
        # --------------------------------------------------------------------------------------------------------------

        self.width = width
        self.height = heigth
        self.size = font_size

        self.content = self.element_search()

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o elemento de busca.
    #
    # --------------------------------------------------------------------------------------------------------------

    def element_search(self):
        self.__search = self.content_field_search()

        return ft.Container(
            expand=True,
            height=self.height,
            content=ft.Row(
                controls=[
                    ft.IconButton(height=self.height, **ButtonStyle.button_search_icon, on_click=self.get_search),
                    self.__search
                ],
                expand=True
            ),
            **MenuStyle.container_search
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o elemento TextField do elemento busca.
    #
    # --------------------------------------------------------------------------------------------------------------

    def content_field_search(self):
        return ft.TextField(expand=True, text_size=self.size, **TextField.textfield_search)

    # --------------------------------------------------------------------------------------------------------------
    #
    # Funções da classe.
    #
    # --------------------------------------------------------------------------------------------------------------

    def get_search(self, e: ft.ControlEvent):
        value = self.__search.value
        return value

    @property
    def search_value(self):
        return self.__search.value

    @search_value.setter
    def search_value(self, value: str):
        self.__search.value = value




# def funcao_teste(page: ft.Page):
#     page.title = "teste de selection box"
#     page.padding = ft.padding.all(0)
#
#     search = Search()
#
#     def mostar(event: ft.ControlEvent):
#         print(search.search_value)
#
#     btn = ft.Button(text="exibir", on_click=mostar)
#
#     container1 = ft.Container(expand=1, bgcolor="orange", content=ft.Row(controls=[search, btn]))
#     container2 = ft.Container(expand=8, bgcolor="red")
#     container3 = ft.Container(expand=1, bgcolor="blue")
#
#     page.add(ft.Column(
#         controls=[
#             container1,
#             container2,
#             container3
#         ],
#         expand=True,
#         spacing=0
#     ))
#
#