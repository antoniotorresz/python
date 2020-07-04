import sys

class sistema_luces(object):

    ventana_luces = object()

    def crear_slider(self):
        self.slider = Scale(self.ventana_luces, from_ = 1, to = 10, orient = "horizontal", showvalue = 0)
        self.slider.bind('<ButtonRelase-1>', self.slider_soltar())
        self.slider.place(x = 10, y = 10 )

        self.slider2 = Scale(self.ventana_luces, from_ = 1, to = 10, orient = "horizontal", showvalue = 0)
        self.slider2.bind('<ButtonRelase-1>', self.slider_soltar())
        self.slider2.place(x = 10, y = 10 )


    def mostrar_ventana(self, principal):
        ventana_luces = Toplevel(principal)
        ventana_luces.geometry("400x300")
        ventana_luces.title("SISTEMA DE LUCES")
        ventana_luces.grab_set()
        self.crear_slider()
        self.crear_btns()

    def slider_soltar(self, event):
        print(self.slider.get())
    def salir(self):
        self.ventana_luces.destroy()
    def crear_btns(self):
        self.btnSalir = Button(self.ventana_luces, text = "SALIR DEL SISTEMA LUCES", command=lambda : self.salir())
        self.apagarTodas = Button(self.ventana_luces, text = "APAGAR TODAS", command=lambda : self.apagarTodas())
        self.encenderTodas = Button(self.ventana_luces, text = "ENCENDER TODAS", command=lambda : self.encenderTodas())

        self.btnSalir.place(x = 200, y = 10)
        self.apagarTodas.place(x = 200, y = 50)
        self.encenderTodas.place(x = 200, y = 100)

    def apagarTodas(self):
        self.slider.set(1)
        self.slider2.set(1)
    def encenderTodas(self):
        self.slider.set(1)
        self.slider2.set(1)
    def apagar_slider(self):
        self.slider.set(1)
    def prender_slider(self):
        self.slider.set(10)

    def apagar_slider2(self):
        self.slider2.set(1)
    def prender_slider2(self):
        self.slider2.set(10)



def main():
    principal = Tk()
    principal.geometry("400x300")
    principal.resizable(0,0)
    luces = sistema_luces()
    principal.title("AUTOMATIZACIÓN DE SITE")

    btnLuces = Button(principal, command=lambda : luces.mostrar_ventana(principal))
    btnCerrar = Button(principal, text = "Cerrar", command=lambda : cerrar(principal))
    btnLuces.place(x = 10, y = 10)
    principal.mainloop()

if __name__ == "__main__":
    try:
        if sys.version == 3:
            from tkinter import *
            from tkinter import ttk
        else:
            from tkinter import *
            from tkinter import ttk
        main()            
    except Exception as e:
        print("Error: {}".format(e))
