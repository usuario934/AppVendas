import flet as ft


class Selection(ft.Stack):
    def __init__(self,
                 id: str,
                 text: str = "Selecione o item",
                 width: int = 220,
                 height: int = 40,
                 height_options: int = 25,
                 spacing: int = 50,
                 padding_container: int | float | ft.Padding = 10,
                 lista_valores: list = None,
                 font_size: int | float = 12, **kw):
        super().__init__(**kw)

        #--------------------------------------------------------------------------------------------------------------
        #
        # Atribuição das variaveis de customização do container.
        #
        # --------------------------------------------------------------------------------------------------------------

        self.text = text
        self.width = width
        self.height = height
        self.font = font_size
        self.spacing = spacing
        self.padding = padding_container
        self.height_options = height_options
        self.clip_behavior = ft.ClipBehavior.NONE

        self.__selection = self.create_selection()
        self.__container_options = self.options(lista_valores)

        self.__selection.height = height
        self.data = {
            "id": id,
            "value": None
        }

        self.add_components()

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar os elementos ao Container Selection.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_components(self):
        self.controls = [
            self.__selection,
            self.__container_options
        ]

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o TextField do Seletion.
    #
    # --------------------------------------------------------------------------------------------------------------

    def create_selection(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.TextField(
                        hint_text=self.text,
                        expand=True,
                        border_color="transparent",
                        read_only=True,
                        enable_interactive_selection=False,
                        text_size=self.font,
                        content_padding=self.padding
                    ),
                    ft.IconButton(
                        height=self.height,
                        icon=ft.Icons.ARROW_DROP_DOWN,
                        padding=0,
                        on_click=self.exibir
                    )
                ],
                expand=True,
                spacing=0
            ),
            border=ft.border.all(2, "#cccccc"),
            border_radius=ft.border_radius.all(4),
            bgcolor="white",
            width=self.width
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o Container das opções do Selection
    #
    # --------------------------------------------------------------------------------------------------------------

    def options(self, lista_itens: list):
        return ft.Container(
            visible=False,
            width=self.width,
            content=ft.Column(
                controls=[
                    *[self.option_default(value) for value in lista_itens]
                ],
                spacing=1,
                scroll=ft.ScrollMode.ADAPTIVE
            ),
            border=ft.border.all(2, "#cccccc"),
            border_radius=ft.border_radius.all(4),
            left=0,
            top=self.spacing,
            bgcolor="white"
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o itens de opções do Selection.
    #
    # --------------------------------------------------------------------------------------------------------------

    def option_default(self, txt: str):
        return ft.TextButton(
            height=self.height_options,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=2)
            ),
            content=ft.Text(
                expand=True,
                value=txt,
                text_align=ft.TextAlign.LEFT,
                width=self.width,
                size=self.font
            ),
            on_click=self.inserir
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Funções da classe.
    #
    # --------------------------------------------------------------------------------------------------------------

    def exibir(self, e: ft.ControlEvent):
        self.__container_options.visible = not self.__container_options.visible

        if self.__container_options.visible:
            self.ajuste_tamanho()
        else:
            self.height = self.__selection.height
        self.update()


    def inserir(self, e: ft.ControlEvent):
        self.__selection.content.controls[0].value = e.control.content.value
        self.data["value"] = e.control.content.value
        self.exibir(e)


    def ajuste_tamanho(self):
        container = self.__container_options.content.controls
        count = self.__selection.height + (self.__container_options.top / 2)

        for child in container:
            count += child.height
            if count < 300:
                self.height = count
            else:
                self.height = 300
                self.__container_options.height = 300


    @property
    def value_select(self):
        return self.__selection.content.controls[0].value

    def set_value(self, value: str):
        self.__selection.content.controls[0].value = value
        self.data["value"] = value
        self.update()






# def funcao_teste(page: ft.Page):
#     page.title = "teste de selection box"
#     page.padding = ft.padding.all(0)
#
#     lista1 = ["caixa", "arroz", "estante", "caixa", "arroz", "estante",  "caixa", "arroz", "estante"]
#
#     select = Selection(lista_valores=lista1, width=150, height=30, padding_container=ft.padding.symmetric(2, 10), spacing=32)
#     select2 = Selection(lista_valores=lista1, width=150, height=30, padding_container=ft.padding.symmetric(2, 10),
#                        spacing=32)
#     container_selection = ft.Container(content=select, border=ft.border.all(1, "red"))
#
#     def exibir(event: ft.ControlEvent):
#         print(select.value_select)
#
#     btn = ft.Button(text="mostrar valor selecao", on_click=exibir)
#
#     container1 = ft.Container(expand=4, bgcolor="orange", content=ft.Row(controls=[container_selection, btn]), alignment=ft.alignment.top_left)
#     container2 = ft.Container(expand=2, bgcolor="red")
#     container3 = ft.Container(expand=2, bgcolor="blue")
#
#     col = ft.Column(
#         controls=[
#             ft.Stack(controls=[
#                 ft.Column(
#                     controls=[
#                         ft.Divider(height=40, color="transparent"),
#                         ft.Container(expand=4, bgcolor="blue"),
#                         ft.Container(expand=1, bgcolor="red"),
#                     ],spacing=0
#                 ),
#                 ft.Container(bgcolor="orange", height=50),
#                 ft.Row(controls=[select, select2, btn], right=20, top=10, vertical_alignment=ft.CrossAxisAlignment.START)
#             ],
#             expand=True)
#         ],
#         expand=True,
#         spacing=0
#     )
#
#     col2 = ft.Column(
#         expand=True,
#         controls=[
#             container1,
#             container2,
#             container3
#         ]
#     )
#
#     page.add(col2)
#
#
# ft.app(target=funcao_teste)