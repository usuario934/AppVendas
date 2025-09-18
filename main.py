import json
import flet as ft

from css import SidebarStyle
from css import ButtonStyle
from css import MenuStyle
from AppDesktop.components.SearchBox import Search
from AppDesktop.components.Dropdown import DropdownApp
from AppDesktop.components.ContainerWithLegend import ContainerContents
from AppDesktop.components.CustomTable import CustomTable, Table
from time import sleep

class MenuSideBar(ft.Row):
    def __init__(self, option_menu: list = None, option_submenu: dict = None):
        super().__init__(**SidebarStyle.container_sidebar2)

        self.submenu = option_submenu
        self.menu = self.create_principal_menu(option_menu)
        self._resize_content_menu()

        self.controls = [
            self.menu
        ]

    def create_principal_menu(self, lista: list):
        return ft.Container(
            content=ft.Column(controls=[
                ft.IconButton(icon=ft.Icons.MENU_ROUNDED, icon_color="white", on_click=lambda y: self.collapse(y, self.menu, 50, 220)),
                ft.Divider(height=2, color="#515B6E"),
                ft.Column(
                    controls=[
                        *[self.add_items_menu(item) for item in lista]
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                ),
                ft.Divider(height=2, color="#515B6E"),
            ]),
            **SidebarStyle.menu
        )

    def create_additional_content(self, elem: dict, parent: str):
        container = None

        if parent in elem:
            container =  ft.Container(
                content=ft.Column(
                    controls=[
                        ft.IconButton(icon=ft.Icons.CLOSE, icon_size=12, icon_color="white", on_click=self.close),
                        ft.Divider(height=2, color="#515B6E"),
                        *[self.add_items_content(item) for item in elem[parent]]
                    ],
                    spacing=1,
                    horizontal_alignment=ft.CrossAxisAlignment.END
                ),
                **SidebarStyle.content_sidebar
            )
        else:
            container = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.IconButton(icon=ft.Icons.CLOSE, icon_size=12, icon_color="white", on_click=self.close),
                        ft.Divider(height=2, color="#515B6E"),
                        ft.Text(value="Vazio", color="white", text_align="left", width=200, no_wrap=True)
                    ],
                    spacing=1,
                    horizontal_alignment=ft.CrossAxisAlignment.END
                ),
                **SidebarStyle.content_sidebar)

        return container

    def add_items_menu(self, elem: dict):
        btn_css: dict = {
            "content": ft.Row(
                controls=[
                  ft.Image(src=elem["icon"], width=25, height=25),
                  ft.Text(elem["title"])
                ],
                spacing=20
            ),
            "width": self.width,
            "height": 50,
            "style": ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: "#515B6E"}, **ButtonStyle.button_menu),
            "on_click":self._change_btn_menubar
        }

        element = ft.TextButton()
        for key, value in btn_css.items():
            setattr(element, key, value)

        return element

    def add_items_content(self, lista: dict):
        return ft.TextButton(
            content=ft.Text(value=lista["title"], no_wrap=True),
            on_click=lambda z: self.close(z),
            style=ft.ButtonStyle(**ButtonStyle.button_content),
            width=200,
            height=40
        )

    def collapse(self, e: ft.ControlEvent, target: object, min: int, max: int):
        target.width = max if target.width == min else min
        self.update()

    def _change_btn(self, event: ft.ControlEvent, color_selected: str, color_default):
        list_element_container = event.control.parent.controls

        for item in list_element_container:
            if isinstance(item, ft.TextButton):
                item.style.bgcolor[ft.ControlState.DEFAULT] = color_default

        event.control.style.bgcolor[ft.ControlState.DEFAULT] = color_selected
        self.update()

    def _change_btn_menubar(self, e: ft.ControlEvent):
        self._change_btn(e, "#515B6E", "transparent")
        self.close(e)

        parent = e.control.content.controls[1].value

        self.content = self.create_additional_content(self.submenu, parent)
        if len(self.controls) < 2:
            self.controls.append(self.content)
            self.update()

        sleep(0.1)
        self.collapse(e, self.content, 0, 200)

    def close(self, e: ft.ControlEvent):
        if len(self.controls) == 2:
            self.collapse(e, self.content, 0, 200)

            sleep(0.5)
            self.controls.remove(self.controls[1])

    def _resize_content_menu(self):
        container = self.menu.content.controls[2]
        container_height = 0

        if len(container.controls) < 10:
            for child in container.controls:
                container_height += child.height

            container.height = int(container_height) + (len(container.controls) * 10)
        else:
            container.expand = True



class MenuTop(ft.Container):
    def __init__(self):
        super().__init__(**MenuStyle.container_menu_top)


        self.__terminal = self.create_element_text("Terminal")
        self.__caixa = self.create_element_text("Caixa")
        self.__host = self.create_element_text("Localhost")
        self.__log = self.create_element_text("User_log")

        self.create_itens_menu()


    def create_itens_menu(self):
        self.content = ft.Row(
            controls=[
                self.__terminal,
                self.__caixa,
                self.__host,
                self.__log
            ]
        )

    def create_element_text(self, txt: str):
        return ft.Row(
            controls=[
                ft.Text(
                    value=txt,
                    expand=True,
                    style=ft.TextStyle(size=12),
                    color="#777777",
                    text_align=ft.TextAlign.LEFT
                ),
                ft.Image(src="assets/icon-separador.png", scale=1)
            ]
        )


    @property
    def terminal(self):
        return self.__terminal.controls[0].value

    @terminal.setter
    def terminal(self, value: str):
        self.__terminal.controls[0].value = value

    @property
    def caixa(self):
        return self.__caixa.controls[0].value

    @caixa.setter
    def caixa(self, value: str):
        self.__caixa.controls[0].value = value

    @property
    def host(self):
        return self.__host.controls[0].value

    @host.setter
    def host(self, value: str):
        self.__host.controls[0].value = value

    @property
    def log(self):
        return self.__log.controls[0].value

    @log.setter
    def log(self, value: str):
        self.__log.controls[0].value = value



class MenuBottom(ft.Container):
    def __init__(self):
        super().__init__(**MenuStyle.container_menu_bottom)

        self.__banco = self._create_element_text("Banco:", "Tecno-tec")
        self.__versao = self._create_element_text("Versão:", "1.0.0")
        self.__dt_atualizado = self._create_element_text("Atualizado em:", "22/05/2025 -- 13:34:50")

        self.create_itens_menu()

    def create_itens_menu(self):
        self.content = ft.Row(
            controls=[
                self.__banco,
                self.__versao,
                self.__dt_atualizado
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=20
        )

    def _create_element_text(self, txt: str, content: str):
        return ft.Row(
            controls=[
                ft.Text(
                    value=txt,
                    expand=True,
                    style=ft.TextStyle(size=12),
                    color="#777777",
                    text_align=ft.TextAlign.LEFT
                ),
                ft.Text(
                    value=content,
                    expand=True,
                    style=ft.TextStyle(size=12),
                    color="#AEAEAE",
                    text_align=ft.TextAlign.LEFT
                ),
            ],
            spacing=4
        )

    @property
    def banco(self):
        return self.__banco.controls[1].value

    @banco.setter
    def banco(self, value: str):
        self.__banco.controls[1].value = value

    @property
    def versao(self):
        return self.__versao.controls[1].value

    @versao.setter
    def versao(self, value: str):
        self.__versao.controls[1].value = value

    @property
    def atualizacao(self):
        return self.__dt_atualizado.controls[1].value

    @atualizacao.setter
    def atualizacao(self, value: str):
        self.__dt_atualizado.controls[1].value = value


def main(page: ft.Page) -> None:

    page.title = "App principal"
    page.window.maximized = True
    page.padding = 0


    def config_application(reference: str):
        with open("contents.json", encoding="UTF-8") as file:
            arq = json.load(file)

            return arq.get(reference)

    def mostrar(e: ft.ControlEvent):
        print(e)
        dropdown.exibir(e)

    def exibir_valores(e: ft.ControlEvent):
        print(container3.get_all)


    def exibir_dados_tabela(e: ft.ControlEvent):
        print(table.get_data)



    lista1 = [
        {
            "title": "Abrir caixa",
            "action": mostrar
        },
        {
            "title": "Fechar caixa",
            "action": mostrar
        },
        {
            "title": "Consultar caixa",
            "action": mostrar
        },
        {
            "title": "Reabrir caixa",
            "action": mostrar
        }
    ]

    select_itens = ["Norte", "Sul", "Leste", "Oeste"]
    select_itens_2 = ["Nacional", "Estrangeiro"]

    radio_itens = [
        {
            "value": "parceiro",
            "label": "Parceiro"
        },
        {
            "value": "concorrente",
            "label": "Concorrente"
        },
        {
            "value": "associado",
            "label": "Associado"
        }
    ]

    check_itens = [
        {
            "id": "solteiro",
            "label": "Solteiro(a)",
            "size": 85
        },
        {
            "id": "casado",
            "label": "Casado(a)",
            "size": 85
        },
        {
            "id": "viuvo",
            "label": "Viuvo(a)",
            "size": 75
        }
    ]

    lista_col = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"]

    lista_itens = [
        ["valor1aaaaaaaaaaa", "valor2", "valor3", "valor4", "valor5"],
        ["valor6", "valor7", "valor8", "valor9", "valor10"],
        ["valor11", "valor12", "valor13", "valor14", "valor15"],
        ["valor16", "valor17", "valor18", "valor19", "valor20"],
    ]

    # --------------------------------------------------------------------------------------------------------------
    #
    # Elementos principais.
    #
    # --------------------------------------------------------------------------------------------------------------

    sidebar = MenuSideBar(config_application("list_elements_menuSidebar"), config_application("list_elements_contentSidebar"))
    menu_top = MenuTop()
    menu_bottom = MenuBottom()
    search = Search(heigth=30)
    dropdown = DropdownApp(lista_reference=lista1, text="Opções caixa", width=150, height=30, padding=ft.padding.symmetric(0, 8))

    # --------------------------------------------------------------------------------------------------------------
    #
    # Criando elementos container
    #
    # --------------------------------------------------------------------------------------------------------------

    container1 = ContainerContents("c1", "Cadastro")
    col_c1 = ft.Column(
        controls=[
            container1.add_input("input1", "Nome:", "digite seu nome"),
            container1.add_input("input2", "Nome_fantasia:", "fantasia"),
            container1.add_group_checkbox("lista_checkbox_1", check_itens, "column"),
            container1.add_selection("cont_select1", "regiao", select_itens, id="selec1", margin_text=8, width=120)
        ],
        spacing=4
    )
    container1.add_childrens(col_c1)


    container2 = ContainerContents("c2", "Atributos")
    col_c2 = ft.Column(
        controls=[
            container2.add_radio("radio1", radio_itens, "column"),
            container2.add_input("input3", "Cliente", ""),
            container2.add_selection("cont_select2", "Nacionalidade", select_itens_2, id="select2", margin_text=8)
        ],
        spacing=4
    )
    container2.add_childrens(col_c2)


    container3 = ContainerContents("c3", "Contato")
    col_c3 = ft.Column(
        controls=[
            container3.add_input("input4", "Telefone 1", "(xx) xxxxx-xxxx", type_text="number"),
            container3.add_input("input5", "Telefone 2", "(xx) xxxxx-xxxx", type_text="number"),
            container3.add_input("input6", "Telefone 3", "(xx) xxxxx-xxxx", type_text="number")
        ]
    )
    container3.add_childrens(col_c3)
    container3.add_childrens(container3.add_checkbox("check1", "Possui redes sociais?"))

    container4 = ContainerContents("c4", "Contato")
    col_c4 = ft.Column(
        controls=[
            container3.add_input("input7", "Telefone 1", "(xx) xxxxx-xxxx", type_text="number"),
            container3.add_input("input8", "Telefone 2", "(xx) xxxxx-xxxx", type_text="number"),
            container3.add_input("input9", "Telefone 3", "(xx) xxxxx-xxxx", type_text="number")
        ]
    )
    container4.add_childrens(col_c4)
    container4.add_childrens(container4.add_checkbox("check2", "Possui redes sociais?"))

    # --------------------------------------------------------------------------------------------------------------
    #
    # Coluna de Containers com legenda.
    #
    # --------------------------------------------------------------------------------------------------------------

    col_containers = ft.Column(
        controls=[
            ft.Row(
                expand=False,
                controls=[
                    container1,
                    container2
                ],
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            ft.Row(
                expand=False,
                controls=[
                    container3,
                    container4
                ],
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            ft.ElevatedButton("Exibir dados", ft.Icons.DATA_ARRAY,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(4)),
                              on_click=exibir_valores)
        ],
    )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Criação de exemplo da Tabela.
    #
    # --------------------------------------------------------------------------------------------------------------

    table = Table("tb_1", lista_col, lista_itens)
    container_top = CustomTable()

    col_table = ft.Column(
        controls=[
            container_top,
            table,
            ft.ElevatedButton("Exibir dados Tabela", ft.Icons.DATA_ARRAY,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(4)),
                              on_click=exibir_dados_tabela),
            ft.Divider(height=30, color="transparent")
        ]
    )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Coluna principal do app.
    #
    # --------------------------------------------------------------------------------------------------------------
    col_main = ft.Column(
        controls=[
            col_containers,
            col_table
        ],
        scroll=ft.ScrollMode.ADAPTIVE
    )


    col = ft.Column(
        controls=[
            ft.Stack(controls=[
                ft.Column(
                    controls=[
                        ft.Divider(height=50, color="transparent"),
                        menu_top,
                        ft.Container(content=col_main,expand=8, bgcolor="white", height=150, padding=ft.padding.symmetric(2, 14)),
                        menu_bottom,
                    ],spacing=0
                ),
                ft.Container(**MenuStyle.container_menu),
                ft.Row(controls=[search, dropdown], right=20, top=10, vertical_alignment=ft.CrossAxisAlignment.START)
            ],
            expand=True)
        ],
        expand=True,
        spacing=0
    )

    # --------------------------------------------------------------------------------------------------------------
    #
    # pagina principal.
    #
    # --------------------------------------------------------------------------------------------------------------

    page.add(ft.Row(controls=[sidebar, col], expand=True, spacing=0))


ft.app(target=main)