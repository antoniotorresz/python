import sys
import datetime as datetime
#import pymysql
import hashlib
if sys.version == 2:
    from Tkinter import *
else:
    from tkinter import *

class frm_inicio():

    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("300x300")
        self.ventana.title("LOGIN")
    
    def load_form(self):
        self.ventana.mainloop()

    def crear_etiquetas(self):
        lblusuario = Label(self.ventana, "Usuario: ")
        lblpassword = Label(self.ventana, "Passwordd: ")

        lblusuario.place(self.ventana, x = 10, y = 10)
        lblpassword.place(self.ventana, x = 10, y = 30)
    
    def crear_textbox(self):
        txtusuario = Text(self.ventana, width = 10, height = 1)
        txtpassword = Text(self.ventana, width = 10, height = 1)
        txtusuario.place(x = 40, y =10)
        txtpassword.place(x = 40, y =30)
    
    def crear_btns(self):
        btnaceptar = Button(self.ventana, width = 5, height = 1, text = "ACEPTAR", command = lambda: abrir_principal)
        btnsalir = Button(self.ventana, width = 5, height = 1, text = "SALIR", command = lambda: salir)

        btnaceptar.place(x = 40, y = 50)
        btnsalir.place(x = 80, y = 50)
    def salir(self):
        self.ventana.destroy()
        exit()
    def abrir_principal(self):
        pass

        
def main():
    inicio = frm_inicio()
    inicio.crear_etiquetas()
    inicio.crear_textbox()
    inicio.crear_btns()
    inicio.load_form()

"""
Conexion = pymysql.connect(host = "localhost", password = "", db = "site")
cursor = Conexion.cursor()
password = hashlib.sha256()
password.update(b'123')
query = "insert into sesiones(username, password) values ('antonio', {})".format(password.hexdigest())
print("Comando: {}".format(query))
cursor.execute(query)
"""
main()