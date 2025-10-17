from typing import Literal
import flet as ft
from .SelectionBox import Selection


class ContainerContents(ft.Container):
    def __init__(self,
                 id: str,
                 title: str = "title here",
                 bg: str = "white",
                 **kw):
        super().__init__(**kw)

        # --------------------------------------------------------------------------------------------------------------
        #
        # Atribuição das variaveis de customização do container.
        #
        # --------------------------------------------------------------------------------------------------------------

        self.__id = id
        self.__title = title
        self.__bgcolor = bg
        self.__data = {
            "id": self.__id,
            "values": []
        }

        self.__col = ft.Column(
            controls=[],
            spacing=2
        )

        self.container_element = self.__create_element(self.__col, title=self.__title)
        self.__create_container()

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar os elementos ao ContainerContents.
    #
    # --------------------------------------------------------------------------------------------------------------

    def __create_container(self):
        self.content = self.container_element


    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o container com a legenda.
    #
    # --------------------------------------------------------------------------------------------------------------

    def __create_element(self, content: ft.Control, title: str):
        return ft.Stack(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Divider(
                                height=4,
                                color="transparent"
                            ),
                            ft.Container(
                                content=content,
                                border=ft.border.all(2, "#cccccc"),
                                border_radius=ft.border_radius.all(4),
                                bgcolor="transparent",
                                padding=ft.padding.symmetric(10, 8),
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.VerticalDivider(
                                width=5,
                                color="transparent"
                            ),
                            ft.Container(
                                content=ft.Text(expand=True, value=title),
                                padding=ft.padding.symmetric(2, 4),
                                bgcolor=self.__bgcolor
                            )
                        ]
                    )
                ],
            )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar um container de Seleção.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_selection(self,
                      id_select: str,
                      title: str = "select here",
                      lista_valores: list = None,
                      text_size: int | float = 14,
                      margin_text: int = 4,
                      visible: bool = True,
                      disable: bool = False,
                      **kws):
        text = ft.Column(
            controls=[
                ft.Divider(
                    height=margin_text,
                    color="transparent"
                ),
                ft.Text(
                    value=title,
                    size=text_size
                )
            ],
            spacing=0
        )

        select = Selection(lista_valores = lista_valores, **kws)

        container = ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[text, select],
            spacing=6,
            visible=visible,
            disabled=disable,
            data={
                "id": id_select
            }
        )

        return container

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar um container de Texto.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_input(self,
                  id: str = "...",
                  title: str = "...",
                  hint_text: str = "##",
                  font_size: int = 12,
                  width_title: int | float = 100,
                  width_textfield: int | float = 150,
                  visible: bool = True,
                  type_text: Literal["text", "number", "email"] = "text",
                  disable: bool = False):

        def type_field(x = type_text):
            if x == "text":
                pass
            elif x == "number":
                setattr(textfield, "keyboard_type", ft.KeyboardType.NUMBER)
                setattr(textfield, "input_filter", ft.InputFilter(regex_string=r"[0-9]", allow=True))

            elif x == "email":
                setattr(textfield, "keyboard_type", ft.KeyboardType.EMAIL)


        def change_textfield(e: ft.ControlEvent):
            textfield.value = textfield.value
            elem.data["value"] = textfield.value


        textfield = None
        title = ft.Text(
                    value=title,
                    text_align=ft.alignment.center_left,
                    width=width_title
                )

        textfield = ft.TextField(
                    width=width_textfield,
                    height=30,
                    hint_text=hint_text,
                    border=ft.InputBorder.OUTLINE,
                    border_radius=ft.border_radius.all(4),
                    text_size=font_size,
                    text_vertical_align=ft.VerticalAlignment.CENTER,
                    content_padding=ft.padding.symmetric(0, 10),
                    on_change=change_textfield,
                    input_filter=ft.InputFilter(regex_string=r"^[a-zA-Z]*$", allow=True),
                    data={
                        "id_parent": id
                    }
                )
        type_field()

        elem = ft.Row(
            controls=[title, textfield],
            visible=visible,
            disabled=disable,
            data={
                "id": id
            }
        )

        return elem

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar um container de Radio Buttons.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_radio(self,
                  id: str,
                  lista_valores: list,
                  type: Literal["column", "row"] = "column",
                  visible: bool = True,
                  disable: bool = False):
        radio = None

        def change(e: ft.ControlEvent):
            radio.data["value"] = radio.value

        if type == "column":
            radio = ft.RadioGroup(
                content=ft.Column(
                    controls=[
                        *[ft.Radio(value=item["value"], label=item["label"]) for item in lista_valores]
                    ]
                ),
                visible=visible,
                data={
                    "id": id,
                    "value": None
                },
                disabled=disable,
                on_change=change
            )
        else:
            radio = ft.RadioGroup(
                content=ft.Row(
                    controls=[
                        *[ft.Radio(value=item["value"], label=item["label"]) for item in lista_valores]
                    ]
                ),
                visible=visible,
                data={
                    "id": id,
                    "value": None
                },
                on_change=change
            )

        return radio

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar um container de Checkbox.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_checkbox(self, id: str, lb: str, size: int = 140, visible: bool = True, disable: bool = False):
        def change(e: ft.ControlEvent):
            elem_check.data["value"] =  elem_check.value

        elem_check = ft.Checkbox(
            label=lb,
            width=size,
            adaptive=True,
            value=False,
            visible=visible,
            disabled=disable,
            data={
                "id": id,
                "value": False
            },
            on_change=change
        )

        return elem_check

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para adicionar um container de Grupos de Checkbox.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_group_checkbox(self,
                           id: str,
                           lista_valores: list,
                           type: Literal["column", "row"] = "column",
                           visible: bool = True,
                           disable: bool = False):
        container = None

        if type == "column":
            container = ft.Container(
                content=ft.Column(
                    controls=[
                        *[self.add_checkbox(id=item["id"], lb=item["label"], size=item.get("size")) for item in lista_valores]
                    ],
                    spacing=1
                ),
                visible=visible,
                disabled=disable,
                data={
                    "id": id
                }
            )
        else:
            container = ft.Container(
                content=ft.Row(
                    controls=[
                        *[self.add_checkbox(id=item["id"], lb=item["label"], size=item.get("size")) for item in
                          lista_valores]
                    ],
                    spacing=1
                ),
                visible=visible,
                disabled=disable,
                data={
                    "id": id
                }
            )

        return container

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função da classe.
    #
    # --------------------------------------------------------------------------------------------------------------

    def add_childrens(self, child: ft.Control):
        self.__col.controls.append(child)


    def navegando(self, control):
        yield control

        if hasattr(control, "controls") and control.controls:
            for c in control.controls:
                yield from self.navegando(c)

        if hasattr(control, "content") and control.content:
            yield from self.navegando(control.content)



    @property
    def __colletion_child(self):
        self.__data["values"].clear()

        for ctrl in self.navegando(self.__col):                     #type: ignore
            if ctrl.data:
                self.__data["values"].append(ctrl.data)

        return self.__data

    @property
    def get_all(self):
        return self.__colletion_child


    def get_value(self, key: str):
        for ctrl in self.navegando(self.__col):                     #type: ignore
            if ctrl.data and ctrl.data.get("id") == key:
                return ctrl
        return None

    def set_value(self, key: str, attr: Literal["id", "value"],  value):
        for ctrl in self.navegando(self.__col):                     #type: ignore
            if ctrl.data and ctrl.data.get("id") == key and key is not self.__id:
                setattr(ctrl, attr, value)
                ctrl.data[attr] = value






# def funcao_teste(page: ft.Page):
#     page.title = "teste de selection box"
#     page.padding = ft.padding.all(0)
#
#     teste23 = ["1", "teste", "ee"]
#     teste122 = [
#         {
#             "value": "teste1",
#             "label": "t1"
#         },
#         {
#             "value": "teste2",
#             "label": "t2"
#         },
#         {
#             "value": "teste3",
#             "label": "t3"
#         }
#     ]
#
#     checks = [
#         {
#             "id": "check1",
#             "label": "che1",
#             "size": 60
#         },
#         {
#             "id": "check2",
#             "label": "che2",
#             "size": 60
#         },
#         {
#             "id": "check3",
#             "label": "che3",
#             "size": 60
#         }
#     ]
#
#     teste = ContainerContents(id="c0", title="teste aqui")
#
#     col_teste = ft.Column(
#         controls=[
#             teste.add_input(id="input1", title="algo aqui", hint_text="digite o valor"),
#             teste.add_input(id="input2", title="outro aqui", hint_text="escreva algo"),
#             teste.add_input(id="input3", title="outro aqui", hint_text="escreva algo"),
#             teste.add_selection(id_select="container_select1", id="select4", lista_valores=teste23, width=120, height=30, spacing=32),
#             teste.add_checkbox("ch1", "testando checkbox"),
#             teste.add_checkbox("ch2", "testando checkbox 2", size=150),
#             teste.add_group_checkbox("lista_check", lista_valores=checks, type="row")
#         ]
#     )
#
#     teste.add_childrens(col_teste)
#     teste.add_childrens(teste.add_radio("radio1", teste122, type="row"))
#     teste.set_value("c0", "value", True)
#     teste.set_value("check1", "value", True)
#     teste.set_value("ch1", "id", "chi1.1")
#     teste2 = ContainerContents(id="c1")
#     teste2.add_input(id="input3", title="novo campo", hint_text="escreva algo")
#     teste3 = ContainerContents(id="c2")
#     teste4 = ContainerContents(id="c3")
#
#     def exibir_valores(e: ft.ControlEvent):
#         print(teste.get_all)
#         print(teste.get_value("radio1").value)
#
#     container1 = ft.Container(bgcolor="blue",expand=1)
#     container2 = ft.Container(bgcolor="white", expand=8, content=ft.Column(controls=[ft.Row(expand=False, controls=[teste, teste2]), ft.Row(expand=False, controls=[teste3, teste4]), ft.ElevatedButton(text="executar ação", on_click=exibir_valores)], scroll=ft.ScrollMode.ADAPTIVE))
#     container3 = ft.Container(bgcolor="green", expand=1)
#
#     col = ft.Column(
#         controls=[
#             container1,
#             container2,
#             container3
#         ],
#         expand=True,
#         spacing=0
#     )
#
#     page.add(col)
#
#     def buscar():
#         for ctrl in teste.navegando(teste):
#             if ctrl.data != None:
#                 print(f"{type(ctrl)} -> data: {ctrl.data}")
#

# ft.app(target=funcao_teste)

