import flet as ft

class DropdownApp(ft.Stack):
    def __init__(self,
                 text: str = "Selecione a acao",
                 width: int = 220,
                 height: int = 35,
                 height_options: int | float = 30,
                 spacing: int = 40,
                 font_size: int | float = 12,
                 padding: int | float | ft.Padding = 0,
                 lista_reference: list = None,
                 **kw
                 ):
        super().__init__(**kw)

        # --------------------------------------------------------------------------------------------------------------
        #
        # Atribuição das variaveis de customização do container.
        #
        # --------------------------------------------------------------------------------------------------------------

        self.text = text
        self.width = width
        self.height = height
        self.height_options = height_options
        self.padding = padding
        self.font = font_size
        self.gap = spacing
        self.clip_behavior = ft.ClipBehavior.NONE

        self.container_top = self.create_element_top()
        self.container_options = self.options(lista_reference)

        self.container_top.height = height

        self.add_contents()
        self.ajuste_tamanho()

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar os elementos ao container.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_contents(self):
        self.controls = [
            self.container_top,
            self.container_options
        ]

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o elemento do Container topo.
    #
    # --------------------------------------------------------------------------------------------------------------

    def create_element_top(self):
        return ft.Container(
            expand=True,
            content=ft.Row(
                controls=[
                    ft.Text(
                        expand=True,
                        value=self.text,
                        enable_interactive_selection=False,
                        text_align=ft.TextAlign.LEFT,
                        size=self.font
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
            padding=self.padding,
            bgcolor="white",
            width=self.width
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o container das Opções.
    #
    # --------------------------------------------------------------------------------------------------------------

    def options(self, lista_itens: list):
        return ft.Container(
            visible=False,
            content=ft.Column(
                controls=[
                    *[self.option_default(value) for value in lista_itens]
                ],
                spacing=1,
                scroll=ft.ScrollMode.ADAPTIVE
            ),
            top=self.gap,
            border=ft.border.all(2, "#cccccc"),
            border_radius=ft.border_radius.all(4),
            bgcolor="white"
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o elementos padrões de opção.
    #
    # --------------------------------------------------------------------------------------------------------------

    def option_default(self, item: dict):
        return ft.TextButton(
            expand=True,
            width=self.width,
            height=self.height_options,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=2)
            ),
            content=ft.Text(
                value=item["title"],
                text_align=ft.TextAlign.LEFT,
                width=self.width,
                size=self.font
            ),
            on_click=item["action"]
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função da classe.
    #
    # --------------------------------------------------------------------------------------------------------------

    def exibir(self, e: ft.ControlEvent):
        self.container_options.visible = not self.container_options.visible

        if self.container_options.visible:
            self.ajuste_tamanho()
        else:
            self.height = self.container_top.height
        self.update()


    def ajuste_tamanho(self):
        container = self.container_options.content.controls
        count = self.container_top.height + (self.container_options.top / 2)

        for child in container:
            count += child.height
            if count < 300:
                self.height = count
            else:
                self.height = 300
                self.container_options.height = 300





# def funcao_teste(page: ft.Page):
#     page.title = "teste de selection box"
#     page.padding = ft.padding.all(0)
#
#     def mostrar(e: ft.ControlEvent):
#         print(e)
#         drop.exibir(e)
#
#     lista1 = [
#         {
#             "title": "valor1",
#             "action": mostrar
#         },
#         {
#             "title": "valor2",
#             "action": mostrar
#         },
#         {
#             "title": "valor3",
#             "action": mostrar
#         },
#         {
#             "title": "valor4",
#             "action": mostrar
#         },
#         {
#             "title": "valor5",
#             "action": mostrar
#         },
#     ]
#
#
#     drop = DropdownApp(lista_reference=lista1, text="Opções caixa", padding=ft.padding.symmetric(2, 8), width=180)
#
#     container = ft.Container(content=drop, border=ft.border.all(1, "blue"))
#
#     container1 = ft.Container(expand=4, bgcolor="orange", content=ft.Row(controls=[container]))
#     container2 = ft.Container(expand=2, bgcolor="red")
#     container3 = ft.Container(expand=2, bgcolor="blue")
#
#     col = ft.Column(
#         expand=True,
#         controls=[
#             container1,
#             container2,
#             container3
#         ]
#     )
#
#     page.add(col)


# ft.app(target=funcao_teste)