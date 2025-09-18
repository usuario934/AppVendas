from typing import Optional
from AppDesktop.components import SearchBox
import flet as ft


class CustomTable(ft.Container):
    def __init__(self):
        super().__init__()

        # --------------------------------------------------------------------------------------------------------------
        #
        # Classe ainda em desenvolvimento.
        #
        # --------------------------------------------------------------------------------------------------------------

        self.content = self.__create_components()
        self.clip_behavior=ft.ClipBehavior.ANTI_ALIAS

    def __create_components(self):
        return ft.Column(
            controls=[
                self.__create_elements_top()
            ]
        )

    def __create_elements_top(self):
        return ft.Container(
            height=40,
            # border=ft.border.all(2, "blue"),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.Stack(
                height=180,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                controls=[
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("Novo", ft.Icons.ADD_BOX,
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(4)),
                                              disabled=True),
                            ft.ElevatedButton("Relatório", ft.Icons.ASSIGNMENT,
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(4)),
                                              disabled=True),
                            SearchBox.Search(heigth=35),
                            ft.ElevatedButton("Filtro", ft.Icons.FILTER_ALT,
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(4)),
                                              disabled=True)
                        ]
                    ),
                    # self.__create_filter()
                ]
            )
        )


    def __create_filter(self):
        return ft.Column(
            controls=[
                ft.Divider(28, color="transparent"),
                ft.Row(
                    controls=[
                        ft.VerticalDivider(400, color="transparent"),
                        self.__create_components_filter()
                    ]
                )
            ]
        )

    def __create_components_filter(self):
        return ft.Container(
            border=ft.border.all(2, "red"),
            content=ft.Column(
                controls=[
                    ft.Text("o filtro vai aqui"),
                    ft.Text("o filtro vai aqui"),
                    ft.Text("o filtro vai aqui"),
                    ft.Text("o filtro vai aqui")
                ]
            )
        )






class Table(ft.Container):
    def __init__(self, id: str, cols: list[str] = None, list_data: list[list[str]] = None):
        super().__init__()

        # --------------------------------------------------------------------------------------------------------------
        #
        # Atribuição das variaveis de customização do container.
        #
        # --------------------------------------------------------------------------------------------------------------

        self.id = id
        self.list_cols = cols
        self.list_data = list_data
        self.clip_behavior = ft.ClipBehavior.ANTI_ALIAS
        self.border = ft.border.all(2, "#cccccc")
        self.border_radius = ft.border_radius.all(6)
        self.data = {
            "id": id,
            "dt_return": [],
            "dt_error": {}
        }

        # --------------------------------------------------------------------------------------------------------------
        #
        # Função para adicionar os elementos ao container.
        #
        # --------------------------------------------------------------------------------------------------------------

        self.__cols = self.__create_cols(self.list_cols)
        self.content = self.__create_table()

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar a Tabela.
    #
    # --------------------------------------------------------------------------------------------------------------

    def __create_table(self):
        return ft.Row(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                self.__create_components(self.list_data)
            ]
        )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar o componentes de Dados e a adiciona-los a tabela.
    #
    # --------------------------------------------------------------------------------------------------------------


    def __create_components(self, reference: list = None):
        if reference is not None:
            return ft.Column(
                spacing=0,
                controls=[
                    self.__cols,
                    *[self.__create_row(index, content) for index, content in enumerate(reference)],
                ]
            )

        return ft.Column(
                spacing=0,
                controls=[
                    self.__cols,
                    ft.Container(padding=ft.padding.symmetric(20, 0))
                ]
            )

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar as Colunas.
    #
    # --------------------------------------------------------------------------------------------------------------

    def __create_cols(self, list_col: list[str]):
        try:
            content_col = ft.Row(
                height=30,
                controls=[
                    ft.Container(
                        content=ft.Checkbox("", False, width=25, on_change=self.check_all),
                        border=ft.border.only(bottom=ft.BorderSide(2, "#cccccc")),
                        padding=ft.padding.symmetric(2, 5),
                    )
                ],
                spacing=0
            )

            container_icons = ft.Container(
                    width=100,
                    border=ft.border.only(bottom=ft.BorderSide(2, "#cccccc")),
                    padding=ft.padding.symmetric(4, 6),
                    content=ft.Row(
                        spacing=1,
                        controls=[
                            ft.Text(value="Modificar", expand=True, text_align=ft.TextAlign.LEFT, no_wrap=True)
                        ]
                    )
            )

            container_col = ft.Container(
                content=content_col,
                data={
                    "dt_cols": content_col.controls
                }
            )

            for col in list_col:
                dt_col = ft.Container(
                    ink=True,
                    width=100,
                    tooltip=f"Organizar por {col}",
                    border=ft.border.only(bottom=ft.BorderSide(2, "#cccccc")),
                    padding=ft.padding.symmetric(0, 4),
                    content=ft.Row(
                        spacing=1,
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.ARROW_DOWNWARD_ROUNDED,
                                icon_size=14, size_constraints=ft.BoxConstraints(8),
                                hover_color="transparent",
                                selected_icon_color="transparent",
                                disabled=True
                            ),
                            ft.Text(value=col, expand=True, text_align=ft.TextAlign.LEFT, no_wrap=True)
                        ]
                    ),
                    data={
                        "id": f"COL_{list_col.index(col)}_{self.id}"
                    },
                    on_click=lambda x: print(x.control.data["id"])
                )

                gd = ft.GestureDetector(
                    content=ft.VerticalDivider(width=2, thickness=2, color="#cccccc"),
                    drag_interval=10,
                    on_pan_update=self.__move_all_divider,
                    on_hover=self.show_draggable_cursor,
                )

                content_col.controls.append(dt_col)
                content_col.controls.append(gd)
            content_col.controls.append(container_icons)

            return container_col

        except Exception:
            self.data["dt_error"]["TypeError_cols"] = "Error nao construção das colunas!"
            return ft.Text("NONE_cols!", color="red")

    # --------------------------------------------------------------------------------------------------------------
    #
    # Função para criar as Linhas com os dados.
    #
    # --------------------------------------------------------------------------------------------------------------

    def __create_row(self, id: str, data: list[str]):
        try:
            elems = self.__cols.data["dt_cols"]

            components: list = [x for x in elems if x.data]
            count = len(components)

            container_modify = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.EDIT, icon_size=15, padding=0),
                        ft.IconButton(icon=ft.Icons.DELETE, icon_size=15, padding=0)
                    ],
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                padding=ft.padding.symmetric(0, 10)
            )


            content_row = ft.Text("NONE!", color="red")

            if len(data) == count:
                content_row = ft.Row(
                    height=25,
                    controls=[
                        ft.Container(
                            content=ft.Checkbox("", False, width=25, on_change=self.__selected_component),
                            padding=ft.padding.symmetric(0, 5),
                        )
                    ],
                    data={
                        "id": f"row_{id}",
                        "dt_row": []
                    },
                    spacing=0
                )

                content_row.id = id

                for id_gd, value in enumerate(data):
                    dt_cell = ft.Container(
                                content=ft.Text(value, expand=True, text_align=ft.TextAlign.LEFT, no_wrap=True),
                                width=100,
                                padding = ft.padding.symmetric(0, 4),
                                data={
                                    "value": value
                                }
                            )

                    gd_cell_row = ft.GestureDetector(
                        content=ft.VerticalDivider(width=2, thickness=2, color="#cccccc"),
                        drag_interval=10,
                        on_pan_update=None,
                        on_hover=lambda x: ft.MouseCursor.BASIC,
                    )

                    gd_cell_row.id = id_gd

                    content_row.controls.append(dt_cell)
                    content_row.data["dt_row"].append(dt_cell.content.value)
                    content_row.controls.append(gd_cell_row)

                content_row.controls.append(container_modify)

            return content_row

        except Exception as error:
            self.data["dt_error"]["TypeError_row"] = f"{error}"
            return ft.Text("NONE!_row", color="red")

    # --------------------------------------------------------------------------------------------------------------
    #
    # Funções da classe.
    #
    # --------------------------------------------------------------------------------------------------------------

    def navegador(self, control):
        yield control

        if hasattr(control, "controls") and control.controls:
            for c in control.controls:
                yield from self.navegador(c)

        if hasattr(control, "content") and control.content:
            yield from self.navegador(control.content)

    # --------------------------------------------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------------------------------------------


    def _filter_components(self, target: Optional[ft.Control] = None, instance: Optional[ft.Control] = None):
        list_components: list = []

        if instance is not None:
            for ctrl in self.navegador(target):
                if isinstance(ctrl, instance):
                    list_components.append(ctrl)

        else:
            for ctrl in self.navegador(target):
                list_components.append(ctrl)

        return list_components

    # --------------------------------------------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------------------------------------------

    def __move_all_divider(self, e: ft.DragUpdateEvent):
        list_reference = self.content.controls[0].controls
        pos_gd = self.__cols.content.controls.index(e.control)

        self.move_vertical_divider(e)

        for row in list_reference:
            if isinstance(row, ft.Row):
                try:
                    bar = row.controls[pos_gd]
                    element_anterior = row.controls[pos_gd - 1]
                except IndexError:
                    continue

                if isinstance(bar, ft.GestureDetector):
                    element_anterior.width = max(50, min(300, element_anterior.width + e.delta_x))
                    element_anterior.update()

                    bar.delta_x = e.delta_x

    # --------------------------------------------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------------------------------------------

    def check_all(self, e: ft.ControlEvent):
        checks = self._filter_components(self.content, ft.Checkbox)
        list_value = self._filter_components(self.content, ft.Row)

        if e.control.value:
            self.data["dt_return"].clear()

            for item in list_value:
                if item.data:
                    self.data["dt_return"].append((item.id, item))

            for ctrl in checks:
                ctrl.value = e.control.value
                ctrl.update()

        else:
            self.data["dt_return"].clear()
            for ctrl in checks:
                ctrl.value = e.control.value
                ctrl.update()

    # --------------------------------------------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------------------------------------------

    def __selected_component(self, e: ft.ControlEvent):
        component = e.control.parent
        parent = component.parent
        check_all = self._filter_components(self.content, ft.Checkbox)

        if e.control.value:
            self.data["dt_return"].append((parent.id, parent))
        else:
            setattr(check_all[0], "value", False)
            check_all[0].update()
            self.data["dt_return"].remove((parent.id, parent))

    # --------------------------------------------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------------------------------------------

    def get_row(self, id_row: str):
        rows = self._filter_components(self.content, ft.Row)
        response = None

        for ctrl in rows:
            if ctrl.data and ctrl.data["id"] == id_row:
                response = ctrl.data

        return response

    # --------------------------------------------------------------------------------------------------------------
    #
    # Funções de retorno da classe.
    #
    # --------------------------------------------------------------------------------------------------------------

    @property
    def get_all_rows(self):
        rows = self._filter_components(self.content, ft.Row)
        response: list = []

        for ctrl in rows:
            if ctrl.data:
                response.append(ctrl.data)

        return response


    @property
    def get_data(self):
        return self.data


    @staticmethod
    def move_vertical_divider(e: ft.DragUpdateEvent):
        parent = e.control.parent
        list_child = parent.controls

        child = list_child[list_child.index(e.control) - 1]
        child.width = max(50, min(300, child.width + e.delta_x))

        child.update()


    @staticmethod
    def show_draggable_cursor(e: ft.HoverEvent):
        e.control.mouse_cursor = ft.MouseCursor.RESIZE_LEFT_RIGHT
        e.control.update()











# def main(page: ft.Page):
#     page.title = 'Teste'
#
#     lista_col = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"]
#     lista_itens = [
#         ["valor1aaaaaaaaaaa", "valor2", "valor3", "valor4", "valor5"],
#         ["valor6", "valor7", "valor8", "valor9", "valor10"],
#         ["valor11", "valor12", "valor13", "valor14", "valor15"],
#         ["valor16", "valor17", "valor18", "valor19", "valor20"],
#     ]
#     lista_teste = None
#
#     teste_container = Table("tb1", lista_col, lista_itens)
#     teste_container_top = CustomTable()
#
#     def mostrar(e: ft.ControlEvent):
#         print(teste_container.get_data)
#
#     btn = ft.ElevatedButton("Mostrar", on_click=mostrar)
#
#     page.add(ft.Container(
#         content=ft.Column(
#             controls=[teste_container_top, teste_container, btn]
#         )
#     ))
#
# ft.app(main)