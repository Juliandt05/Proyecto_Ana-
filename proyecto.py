import flet as ft

def main(page: ft.Page):
    nombre_textfield = ft.TextField(label="Nombre")
    contrasena_textfield = ft.TextField(label="Contraseña")

    def comprobar_usuario_contra(e):
        vusuario = []
        contador = 0
        f = open("fichero.txt","r")
      
        for linea in f:
            l = linea.replace("\n", "")
            vusuario.append(l)
        if contador<=3:
            if vusuario.count(nombre_textfield.value)>0 and vusuario.count(contrasena_textfield.value)>0:
                alerta = ft.AlertDialog(title=ft.Text("Inicio de sesión conseguido"))
                page.dialog = alerta
                alerta.open = True
            else:
                alerta_fallido = ft.AlertDialog(title=ft.Text("Inicio de sesión fallido"))
                page.dialog = alerta_fallido
                alerta_fallido.open = True
                contador+=1
            page.update()
            f.close
        else:
            alerta_fallido = ft.AlertDialog(title=ft.Text("Terminado intentos"))
            page.dialog = alerta_fallido
            alerta_fallido.open = True

    boton = ft.FilledButton(text="Iniciar Sesión", on_click=comprobar_usuario_contra)

    page.add(boton,nombre_textfield,contrasena_textfield)
ft.app(target=main)