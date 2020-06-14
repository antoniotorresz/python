import sys
class string_operations():
    base_string = ""
    output_string = ""
    def get_reverse(self):
        base_list = list(self.base_string)
        reverse = ""
        for i in range(len(base_list)):
            reverse += base_list[(len(base_list) - 1) - i]
        self.output_string = reverse
    def sust_vocals(self):
        new_word = ""
        for letter in self.base_string.lower():
            if letter == 'a':
                letter = '4'
            if letter == 'e':
                letter = '3'
            if letter == 'i':
                letter = '1'
            if letter == 'o':
                letter = '0'
            if letter == 'u':
                letter = '5'
            new_word += letter
        self.output_string = new_word   
    def word_to_upper_lower(self):
        new_word = ""
        for letter in self.base_string:
            if str(letter).islower():
                new_word += letter.upper()
            elif str(letter).isupper():
                new_word += letter.lower()
            else:
                new_word += letter
        self.output_string = new_word
def calculate(option, text):
    op = string_operations()
    op.base_string = text
    if option == 1:
        op.get_reverse()
    if option == 2:
        op.output_string = text.upper()
    if option == 3:
        op.output_string = text.lower()
    if option == 4:
        op.sust_vocals()
    if option == 5:
        op.word_to_upper_lower()
    lbl_res['text'] = "Resultado: {}".format(op.output_string)
if __name__ == "__main__":
    try:
        if sys.version_info[0] == 3:
            from tkinter import *
        else:
            from Tkinter import *    
        root = Tk()
        root.title("Operaciones con Strings")
        root.resizable(0,0)
        root.config(bg = "#01579B")
        root.geometry("360x150")
        miFrame = Frame(root, width = 360, height = 480)
        miFrame.pack()
        cuadroTexto = Entry(miFrame)
        cuadroTexto.grid(row=0, column=1, sticky='w')
        lbl_text = Label(miFrame, text="Palabra", font=("Calibri", 12))
        lbl_text.grid(row=0, column=0, sticky='w')
        btn_inverse = Button(miFrame, text = "INVERSO", command=lambda:calculate(1, cuadroTexto.get()))
        btn_upper = Button(miFrame, text = "MAYÚSCULAS", command=lambda:calculate(2, cuadroTexto.get()))
        btn_lower = Button(miFrame, text = "MINUSCULAS", command=lambda:calculate(3, cuadroTexto.get()))
        btn_vocals = Button(miFrame, text = "SUSTITUCIÓN", command=lambda:calculate(4, cuadroTexto.get()))
        btn_uprlwr = Button(miFrame, text = "MAYUSCULAS - MINUSCULAS", command=lambda:calculate(5, cuadroTexto.get()))
        btn_exit = Button(miFrame, text = "SALIR", command=lambda: exit())          
        btn_inverse.grid(row=1, column=0, sticky='w')
        btn_upper.grid(row=1, column=1, sticky='w')
        btn_lower.grid(row=2, column=0, sticky='w')
        btn_vocals.grid(row=2, column=1, sticky='w')
        btn_uprlwr.grid(row=3, column=0, sticky='w')
        btn_exit.grid(row=3, column=1, sticky='w')
        lbl_res = Label(miFrame, text="Resultado:", font=("Calibri", 12))
        lbl_res.grid(row=4, column=0, sticky='w')    
        root.mainloop()    
    except Exception as e:
        print("Error: {}".format(e))