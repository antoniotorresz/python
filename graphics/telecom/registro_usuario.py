import sys
import pymysql
import datetime
import hashlib
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class ventana:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.strUsuario = tk.StringVar()  
        self.strPwd = tk.StringVar()  
        
        top.geometry("300x300+317+154")
        top.minsize(1, 1)
        top.resizable(0, 0)
        top.title("REGISTRO DE USUARIO")
      

        self.lblusuario = tk.Label(top)
        self.lblusuario.place(relx=0.133, rely=0.267, height=28, width=59)
        self.lblusuario.configure(text='''Usuario:''')

        self.txtusuario = tk.Entry(top)
        self.txtusuario.place(relx=0.4, rely=0.267,height=29, relwidth=0.42)
        self.txtusuario.configure(background="white")
        self.txtusuario.configure(font="TkFixedFont")
        self.txtusuario.configure(textvariable=self.strUsuario)

        self.txpassword = tk.Entry(top)
        self.txpassword.place(relx=0.4, rely=0.433,height=29, relwidth=0.42)
        self.txpassword.configure(background="white")
        self.txpassword.configure(font="TkFixedFont")
        self.txpassword.configure(selectbackground="#c4c4c4")
        self.txpassword.configure(textvariable = self.strPwd)
        self.txpassword.configure(show = "*")

        self.lblpassword = tk.Label(top)
        self.lblpassword.place(relx=0.133, rely=0.433, height=28, width=69)
        self.lblpassword.configure(activebackground="#f9f9f9")
        self.lblpassword.configure(cursor="fleur")
        self.lblpassword.configure(text='''Contraseña:''')

        self.btnaceptar = tk.Button(top)
        self.btnaceptar.place(relx=0.367, rely=0.6, height=28, width=86)
        self.btnaceptar.configure(text='''ACEPTAR''', command = lambda:guardar_usuario(self.strUsuario.get(), self.strPwd.get()))

        self.btnsalir = tk.Button(top)
        self.btnsalir.place(relx=0.767, rely=0.867, height=28, width=63)
        self.btnsalir.configure(text='''SALIR''', command= lambda:destroy_window())

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = ventana (root)
    init(root, top)
    root.mainloop()

w = None
def create_ventana(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_ventana(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = ventana (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_ventana():
    global w
    w.destroy()
    w = None
def guardar_usuario(_user, _password):
    conn = pymysql.connect(host = 'localhost', user = 'ant', password = '', db = 'site')
    cursor = conn.cursor()
    h = hashlib.sha256()
    h.update(_password.encode('utf-8'))
    query = "insert into sesiones (username, password) values ('{}','{}')".format(_user, h.hexdigest())
    cursor.execute(query)
    
if __name__ == '__main__':
    vp_start_gui()




