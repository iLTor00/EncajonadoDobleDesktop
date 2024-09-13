import flet as ft

# Variable para almacenar la caja seleccionada en cada puesto
selected_caja_puesto1 = ft.Ref[ft.Text]()
selected_caja_puesto2 = ft.Ref[ft.Text]()
selected_caja_1 = None
selected_caja_2 = None

# Variable para almacenar mensajes en cada puesto
message_puesto1 = ft.Ref[ft.Text]()
message_puesto2 = ft.Ref[ft.Text]()

def main(page: ft.Page):
    page.title = "Encajonado Doble - Modern UI"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_900  # Fondo oscuro para contrastar con los elementos

    # Función para manejar la selección de caja
    def seleccionar_caja(puesto, caja_num, button):
        global selected_caja_1, selected_caja_2
        if puesto == 1:
            if selected_caja_1:
                selected_caja_1.bgcolor = ft.colors.BLUE_GREY_50  # Resetear la caja anterior
                selected_caja_1.scale = 1
            selected_caja_1 = button
            selected_caja_1.bgcolor = ft.colors.LIGHT_BLUE_ACCENT  # Cambiar color de la caja seleccionada
            selected_caja_1.scale = 1.1  # Aumentar el tamaño de la caja seleccionada
            selected_caja_puesto1.current.value = f"Caja {caja_num} seleccionada"
        else:
            if selected_caja_2:
                selected_caja_2.bgcolor = ft.colors.BLUE_GREY_50  # Resetear la caja anterior
                selected_caja_2.scale = 1
            selected_caja_2 = button
            selected_caja_2.bgcolor = ft.colors.LIGHT_BLUE_ACCENT  # Cambiar color de la caja seleccionada
            selected_caja_2.scale = 1.1  # Aumentar el tamaño de la caja seleccionada
            selected_caja_puesto2.current.value = f"Caja {caja_num} seleccionada"
        page.update()

    # Definir los botones de opción para Ingreso/Egreso con colores visibles
    ingreso_egreso_1 = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="ingreso", label="Ingreso", label_style=ft.TextStyle(color=ft.colors.GREEN)),
                ft.Radio(value="egreso", label="Egreso", label_style=ft.TextStyle(color=ft.colors.RED)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
    )

    ingreso_egreso_2 = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="ingreso", label="Ingreso", label_style=ft.TextStyle(color=ft.colors.GREEN)),
                ft.Radio(value="egreso", label="Egreso", label_style=ft.TextStyle(color=ft.colors.RED)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing= 10
        )
    )

    # Estilos de botones
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=20),
        elevation=6,  # Sombras para el estilo neumorfista
        bgcolor=ft.colors.BLUE_GREY_50,
        side=ft.BorderSide(width=2, color=ft.colors.LIGHT_BLUE_ACCENT),
    )

    # Función para crear una caja seleccionable
    def create_caja_button(puesto, caja_num):
        button = ft.ElevatedButton(
            text=f"Caja {caja_num}",
            on_click=lambda e: seleccionar_caja(puesto, caja_num, button),
            style=button_style
        )
        return button

    # Filas de cajas para Puesto 1 y Puesto 2
    cajas_row_1 = ft.Row(
        [create_caja_button(1, 1), create_caja_button(1, 2), create_caja_button(1, 3)],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        spacing=10
    )

    cajas_row_2 = ft.Row(
        [create_caja_button(2, 4), create_caja_button(2, 5), create_caja_button(2, 6)],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        spacing=10
    )

    # Campo de texto mejorado para ingresar codbar
    codbar_input_puesto1 = ft.TextField(
        label="Ingresar Codbar", 
        width=250, 
        border_radius=20,  # Borde redondeado aplicado al TextField
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
    )

    codbar_input_puesto2 = ft.TextField(
        label="Ingresar Codbar", 
        width=250, 
        border_radius=20,  # Borde redondeado aplicado al TextField
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
    )

    # Sección de Data
    def create_data_section(puesto):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Descripción de Producto", weight=ft.FontWeight.BOLD, size=18, color=ft.colors.WHITE),
                    ft.Text("Insumo Articulo", size=14, color=ft.colors.LIGHT_BLUE_100),
                    ft.Text("Peso Actual: 0 Kg", size=12, color=ft.colors.LIGHT_BLUE_100),
                    ft.Text("Piezas: 0", size=12, color=ft.colors.LIGHT_BLUE_100),
                    ft.Text("Minimo: X Kg - Maximo: X Kg", size=12, color=ft.colors.LIGHT_BLUE_100),
                    ft.Row(
                        [
                            ft.Checkbox(label="Ctrl Homog", label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_100)),
                            ft.Checkbox(label="Validar Peso", label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_100))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(text="EDIT CTRL", bgcolor=ft.colors.LIGHT_BLUE_ACCENT, color=ft.colors.WHITE),
                            ft.ElevatedButton(text="X", bgcolor=ft.colors.RED_ACCENT, color=ft.colors.WHITE)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=15,
            border_radius=20,
            bgcolor=ft.colors.BLUE_GREY_800,
            shadow=ft.BoxShadow(spread_radius=2, blur_radius=10, color=ft.colors.BLACK),
        )

    # Contenedor de mensajes para el usuario
    def create_message_container(message):
        return ft.Container(
            content=message,
            width=300,
            height=50,
            bgcolor=ft.colors.WHITE,
            padding=10,
            border_radius=10,
            alignment=ft.alignment.center,
        )

    # Mensajes para cada puesto
    message_puesto1.current = ft.Text("Mensajes de acciones", color=ft.colors.BLACK)
    message_puesto2.current = ft.Text("Mensajes de acciones", color=ft.colors.BLACK)

    message_container_1 = create_message_container(message_puesto1.current)
    message_container_2 = create_message_container(message_puesto2.current)

    # Puestos en contenedores modernos
    puesto_1 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Puesto 1", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ingreso_egreso_1,
                ft.Text("CAJAS", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                cajas_row_1,
                codbar_input_puesto1,  # Campo de texto para ingresar codbar
                ft.Text("DATA", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                create_data_section(1),
                message_container_1,  # Contenedor de mensajes para Puesto 1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        width=450,
        bgcolor=ft.colors.BLUE_GREY_800,
        border_radius=30,
        padding=20,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.BLACK,
            offset=ft.Offset(5, 5),
        )
    )

    puesto_2 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Puesto 2", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ingreso_egreso_2,
                ft.Text("CAJAS", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                cajas_row_2,
                codbar_input_puesto2,  # Campo de texto para ingresar codbar
                ft.Text("DATA", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                create_data_section(2),
                message_container_2,  # Contenedor de mensajes para Puesto 2
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        width=450,
        bgcolor=ft.colors.BLUE_GREY_800,
        border_radius=30,
        padding=20,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.BLACK,
            offset=ft.Offset(5, 5),
        )
    )

    # Layout general con grid
    page.add(
        ft.Column(
            [
                ft.Text("ENCAJONADO DOBLE", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Row([puesto_1, puesto_2], alignment=ft.MainAxisAlignment.SPACE_AROUND)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30
        )
    )

# Ejecutar la app
ft.app(target=main)
