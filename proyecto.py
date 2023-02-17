import flet as ft



def main(page: ft.Page):
    
    nombre_textfield = ft.TextField(label="Nombre")
    contrasena_textfield = ft.TextField(label="Contraseña")
    txtcontador = ft.TextField(value="0")
    


    def comprobar_usuario_contra(e):
        vusuario = []
        contador = int(txtcontador.value)
        f = open("fichero.txt","r")
        for linea in f:
            l = linea.replace("\n", "")
            vusuario.append(l)
        if contador<3:
            if vusuario.count(nombre_textfield.value)>0 and vusuario.count(contrasena_textfield.value)>0:
                alerta = ft.AlertDialog(title=ft.Text("Inicio de sesión conseguido"))
                page.dialog = alerta
                alerta.open = True
            else:
                alerta_fallido = ft.AlertDialog(title=ft.Text("Inicio de sesión fallido"))
                page.dialog = alerta_fallido
                alerta_fallido.open = True
                contador = contador + 1
                txtcontador.value = contador
            page.update()
            f.close()
        else:
            alerta_fallido_intentos = ft.AlertDialog(title=ft.Text("Terminado intentos"))
            page.dialog = alerta_fallido_intentos
            alerta_fallido_intentos.open = True
            page.update()
        page.update()

   

    boton = ft.FilledButton(text="Iniciar Sesión", on_click=comprobar_usuario_contra)
    print(txtcontador.value)
    page.add(boton,nombre_textfield,contrasena_textfield)

ft.app(target=main)