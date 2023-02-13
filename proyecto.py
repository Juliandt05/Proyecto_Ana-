import flet as ft

def main(page: ft.Page):
    boton = ft.FilledButton(text="Iniciar Sesión")
    
    page.add(boton)
ft.app(target=main)