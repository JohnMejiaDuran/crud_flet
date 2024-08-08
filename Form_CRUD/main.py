import flet as ft

from contact_manager import ContactManager

class Form(ft.UserControl):
    def __init__(self, page):
        super().__init__( expand=True )
        self.page = page
        self.data = ContactManager()

        self.name = ft.TextField(label = "Nombre", border_color = "black", color="black", label_style=ft.TextStyle(color="black"), )
        
        self.age = ft.TextField(label = "Edad", border_color="black",
                                input_filter= ft.NumbersOnlyInputFilter(),
                                max_length=2,
                                color="black", label_style=ft.TextStyle(color="black"))
        
        self.email = ft.TextField(label = "Correo", border_color = "black",color="black", label_style=ft.TextStyle(color="black"))
        
        self.phone = ft.TextField(label = "Telefono", border_color="black",
                                input_filter= ft.NumbersOnlyInputFilter(),
                                max_length=10,color="black", label_style=ft.TextStyle(color="black"))
        self.search_field = ft.TextField(
            label="Buscar por nombre",
            suffix_icon= ft.icons.SEARCH,
            border = ft.InputBorder.UNDERLINE,
            label_style= ft.TextStyle(color="black"),
            color="white"
        )

        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2,"purple"),
            data_row_color={ft.MaterialState.SELECTED: "purple", ft.MaterialState.PRESSED: "green"},
            border_radius=10,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text("Nombre", color="purple", weight="bold")),
                ft.DataColumn(ft.Text("Edad", color="purple", weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Correo", color="purple", weight="bold")),
                ft.DataColumn(ft.Text("Telefono", color="purple", weight="bold"), numeric=True)
            ]
        )

        self.show_data()

        self.form = ft.Container(
            bgcolor = "#ffffff",
            border_radius = 10,
            col = 4,
            content = ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Ingrese sus datos",
                            size=40,
                            text_align="center",
                            font_family="Lucida console"),
                    self.name,
                    self.age,
                    self.email,
                    self.phone,
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextButton(text= "Guardar",
                                            icon=ft.icons.SAVE,
                                            style=ft.ButtonStyle(
                                                color="white", bgcolor="green"
                                            )),
                                ft.TextButton(text= "Actualizar",
                                            icon=ft.icons.UPDATE,
                                            style=ft.ButtonStyle(
                                                color="white", bgcolor="green"
                                            )),
                                ft.TextButton(text= "Borrar",
                                            icon=ft.icons.DELETE,
                                            style=ft.ButtonStyle(
                                                color="white", bgcolor="green"
                                            ))
                        ])
                    )
                ]
            )
        )

        self.table = ft.Container(
            bgcolor = "#ffffff",
            border_radius = 10,
            col = 8,
            content = ft.Column(
                controls=[
                    ft.Container(
                        padding=10,
                        content=ft.Row(
                            controls=[
                                self.search_field,
                                ft.IconButton(tooltip="Editar",
                                              icon=ft.icons.EDIT),ft.IconButton(tooltip="Descargar en PDF",
                                              icon=ft.icons.PICTURE_AS_PDF),ft.IconButton(tooltip="Descargar en EXCEL",
                                              icon=ft.icons.SAVE_ALT),
                            ]
                        )
                    ),
                    ft.Column(
                        expand=True,
                        scroll="auto",
                        controls=[
                            ft.ResponsiveRow([
                                self.data_table        
                            ])                      
                        ]
                    )
                ]
            )
        )

        self.connet = ft.ResponsiveRow(
            controls = [
                self.form,
                self.table
            ]
        )

    def show_data(self):
        self.data_table.rows = []
        for x in self.data.get_contact():
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(x[1])),
                        ft.DataCell(ft.Text(str(x[2]))),
                        ft.DataCell(ft.Text(x[3])),
                        ft.DataCell(ft.Text(str(x[4]))),
                        
                    ]
                )
            )
        self.update()

    def build(self):
        return self.connet
    

def main(page: ft.Page):
    page.bgcolor = "black"
    page.title = "CRUD SQLITE"
    page.window_min_height = 500
    page.window_min_width = 100

    page.add(Form(page))
ft.app(main)