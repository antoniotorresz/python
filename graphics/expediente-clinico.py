import sys
def imprimir(n):
    print(n.get())
def guardar():
    print("Guardado alv")
def main():
    ventana = Tk()
    ventana.title("Expediente clínico")
    ventana.resizable(0,0)
    ventana.geometry("300x300")

    expediente = ttk.Notebook(ventana)
    expediente.grid()

    personales = ttk.Frame(expediente)
    contacto = ttk.Frame(expediente)

    expediente.add(personales, text="Datos personales")
    expediente.add(contacto, text="Datos contacto")
    

    lbl_nombre = Label(personales, text= "*Nombre(s)")
    lbl_nombre.grid(row=1, column=1)
    txt_nombre = Text(personales, width = 10, height = 1)
    txt_nombre.grid(row=1, column = 2)

    lbl_apellidos = Label(personales, text= "*Apellidos")
    lbl_apellidos.grid(row=2, column=1)
    txt_apellidos = Text(personales, width = 10, height = 1)
    txt_apellidos.grid(row=2, column = 2)

    var_genero = StringVar()
    var_genero.set("Género")
    lbl_genero = Label(personales, textvariable = var_genero)
    lbl_genero.grid(row = 3, column = 1)

    cmb_gen = ttk.Combobox(personales, width = 10, height = 1)
    cmb_gen['values'] = ('Masculino', 'Femenino')
    cmb_gen.grid(row = 3, column = 2)

    lbl_ocup = Label(personales, text= "*Ocupación")
    lbl_ocup.grid(row=4, column=1)
    txt_ocup = Text(personales, width = 10, height = 1)
    txt_ocup.grid(row=4, column = 2)

    lbl_edad = Label(personales, text= "*Edad")
    lbl_edad.grid(row=5, column=1)
    spn_edad = ttk.Spinbox(personales, from_=1, to=120)
    spn_edad.grid(row = 5, column = 2)

    rad_talla = IntVar()
    lbl_talla = Label(personales, text="Talla")
    lbl_talla.grid(row=6, column= 1)

    radio_xch = ttk.Radiobutton(personales, text="XS", value=1, var=rad_talla, command=lambda: imprimir(rad_talla))
    radio_xch.grid(row=7, column=1)

    radio_ch = ttk.Radiobutton(personales, text="S", value=2,var=rad_talla, command=lambda: imprimir(rad_talla))
    radio_ch.grid(row=7, column=2)

    radio_m = ttk.Radiobutton(personales, text="M", value=3,var=rad_talla, command=lambda: imprimir(rad_talla))
    radio_m.grid(row=8, column=1)

    radio_l = ttk.Radiobutton(personales, text="L", value=4, var=rad_talla, command=lambda: imprimir(rad_talla))
    radio_l.grid(row=8, column=2)

    radio_xl = ttk.Radiobutton(personales, text="XL", value=5, var=rad_talla, command=lambda: imprimir(rad_talla))
    radio_xl.grid(row=9, column=1)

    var_bool_fuma = BooleanVar()
    lbl_fuma = Label(personales, text='¿Fumador?')
    lbl_fuma.grid(row = 10, column = 1)
    chkb_fuma = ttk.Checkbutton(personales, text="Si", var = var_bool_fuma)
    chkb_fuma.grid(row = 10, column = 2)

    btn_aceptar = Button(personales, text="Guardar", command=lambda: guardar())
    btn_aceptar.grid(row=11, column=1, pady = 20)

    btn_salir= Button(personales, text="Salir", command = lambda : exit())
    btn_salir.grid(row=11, column=2, pady = 20)

    expediente.pack(fill="both", expand=1)

    ventana.mainloop()
if __name__ == "__main__":
    if sys.version_info[0] == 3:
        from tkinter import *
        from tkinter import ttk
    else:
        from Tkinter import *
        from Tkinter import ttk
    main()