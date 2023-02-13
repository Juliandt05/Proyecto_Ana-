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
    nombre_textfield = ft.TextField(label="Nombre")
    contrasena_textfield = ft.TextField(label="Contraseña")
    imagen = ft.Image(src="Logo_empresa.jpg",width=250,height=250)
    page.update()
    colDatos=ft.Column(controls=[nombre_textfield,contrasena_textfield])
    conDatos= ft.Container(content=colDatos,width=250,padding=ft.padding.only(bottom=50))

    page.add(imagen,conDatos)
ft.app(target=main,assets_dir="Imagenes")