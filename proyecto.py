import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Inicio sesión"
    nombre=ft.TextField(label="Nombre", hint_text="Introduzca su nombre",)
    page.padding (50)
  
    page.add(nombre)
ft.app(target=main)