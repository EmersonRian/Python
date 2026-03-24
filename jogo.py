# import tkinter as tk


# janela = tk.Tk()
# janela.title("Janela")
# janela.geometry("720x360")

# def botao_faz():
#     nome = texto_digitado.get()
#     texto_2["text"] = f"Voce {nome}, apertou o botao"


# texto = tk.Label(janela,
# text="Joguinho da Forca\n"
# "______    \n"
# "|    |    \n"
# "|    O    \n"
# "|   /|\\  \n"
# "|   / \\  \n"
# ""
# )

# texto.pack(padx=20)

# texto_digitado = tk.Entry(janela)
# texto_digitado.pack()
# tk.Button(janela,text="Botão", command=botao_faz).pack()

# texto_2 = tk.Label(janela,text="")
# texto_2.pack()


# janela.mainloop()

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.geometry("720x360")

# root.mainloop()

# import tkinter as tk

# def abrir_segunda_janela():
#     # Esconde a janela principal
#     janela1.withdraw()
    
#     # Cria a nova janela
#     janela2 = tk.Toplevel()
#     janela2.title("Segunda Janela")
#     janela2.geometry("300x200")
    
#     # Botão para voltar
#     btn_voltar = tk.Button(janela2, text="Voltar", command=lambda: voltar(janela2))
#     btn_voltar.pack(pady=20)

# def voltar(janela_atual):
#     janela_atual.destroy() # Fecha a segunda janela
#     janela1.deiconify() # Mostra a janela principal novamente

# # Janela Principal
# janela1 = tk.Tk()
# janela1.title("Janela Principal")
# janela1.geometry("300x200")

# btn_ir = tk.Button(janela1, text="Ir para Janela 2", command=abrir_segunda_janela)
# btn_ir.pack(pady=20)

# janela1.mainloop()