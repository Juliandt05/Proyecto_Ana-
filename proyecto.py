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

    txtcontador = ft.TextField(value="0")
    def comprobar_usuario_contra(e):
        vusuario = []
        f = open("fichero.txt","r")
        contador = int(txtcontador.value)
        for linea in f:
            l = linea.replace("\n", "")
            vusuario.append(l)
        if contador<3:
            if vusuario.count(nombre_textfield.value)>0 and vusuario.count(contrasena_textfield.value)>0:
                alerta = ft.AlertDialog(title=ft.Text("Inicio de sesión conseguido"))
                page.dialog = alerta
                alerta.open = True
                alerta_fallido = ft.AlertDialog(title=ft.Text("Inicio de sesión fallido"))
            else:
                page.dialog = alerta_fallido
                contador = contador + 1
                alerta_fallido.open = True
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
    page.add(imagen,nombre_textfield,contrasena_textfield)
ft.app(target=main,assets_dir="Imagenes")