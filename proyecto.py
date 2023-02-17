import flet as ft
import time
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
    contrasena_textfield = ft.TextField(label="Contraseña",password=True, can_reveal_password=True)
    imagen = ft.Image(src="Logo_empresa.jpg",width=250,height=250)
    page.update()
    colDatos=ft.Column(controls=[nombre_textfield,contrasena_textfield])
    conDatos= ft.Container(content=colDatos,width=250,padding=ft.padding.only(bottom=50))
    txtcontador = ft.TextField(value="0")
    def comprobar_usuario_contra(e):
        vusuario = []
        f = open("fichero.txt","r")
        contador = int(txtcontador.value)
        for linea in f:
            l = linea.replace("\n", "")
            vusuario.append(l)
        if contador<2:
            if vusuario.count(nombre_textfield.value)>0 and vusuario.count(contrasena_textfield.value)>0:
                alerta = ft.AlertDialog(title=ft.Text("Inicio de sesión conseguido"))
                page.dialog = alerta
                alerta.open = True
                page.clean()
                
            else:
                alerta_fallido = ft.AlertDialog(title=ft.Text("Inicio de sesión fallido"))
                page.dialog = alerta_fallido
                contador = contador + 1
                alerta_fallido.open = True
                txtcontador.value = contador
            page.update()
            f.close()
        else:
            alerta_fallido_intentos = ft.AlertDialog(title=ft.Text("Usuario Bloqueado"))
            page.dialog = alerta_fallido_intentos
            alerta_fallido_intentos.open = True
            page.update()
            time.sleep(1)
            page.window_close()
            


        page.update()



    boton = ft.ElevatedButton(text="Iniciar Sesión", on_click=comprobar_usuario_contra,color="White")
    print(txtcontador.value)
    page.add(imagen,conDatos,boton)

ft.app(target=main,assets_dir="Imagenes")