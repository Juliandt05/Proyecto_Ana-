import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Inicio sesión"
    page.window_maximizable = False
    page.window_minimized = False
    page.window_max_height = 1500
    page.window_max_width = 1500
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    nombre_textfield = ft.TextField(label="Nombre",width=300)
    contrasena_textfield = ft.TextField(label="Contraseña",width=300)
    imagen = ft.Image(src="Logo_empresa.jpg",width=250,height=250)
    page.update()

    page.add(imagen,nombre_textfield,contrasena_textfield)
ft.app(target=main,assets_dir="Imagenes")