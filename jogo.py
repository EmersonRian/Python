import tkinter as tk
from tkinter import ttk, PhotoImage

janela_principal = tk.Tk() # Criando a janela
janela_principal.title("Janela_Principal") #Colocando um titulo
janela_principal.geometry("400x500+200+200") #Dimençoes da janela
janela_principal.config(bg="lightblue") #conf basica de mudar cor

#metodos para mexer no tamanho da janela e limite dele.
# janela_principal.maxsize(800,600)
# janela_principal.minsize(300,200)
# janela_principal.resizable(False,True)
# janela_principal.state("zoomed")
# janela_principal.attributes("-alpha", 0.7)
janela_principal.iconbitmap("imagens/genga.ico")


msg = tk.Label(janela_principal,text="JANELA PIVETE",bg="lightblue")
msg.pack()


def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Segundamente")
    segunda_janela.config(bg="lightblue")
    segunda_janela.iconbitmap("imagens/genga.ico")


    #Tamanho da janela
    largura_janela = 400
    altura_janela = 300

    #Obter dimenções da tela
    largura_tela = segunda_janela.winfo_screenmmwidth()
    altura_tela = segunda_janela.winfo_screenmmheight()

    #Calculo do posicionamento centralizado da janela
    x = (largura_janela - largura_tela) // 2
    y = (altura_janela - altura_tela) // 2

    #Geometria da janela 2
    segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

def definir_imagens(event):
    largura_janela = janela_principal.winfo.width()
    altura_janela = janela_principal.winfo.height()
    largura_imagen = imagem.width()
    altura_imagen = imagem.heigth()

    posicao_x = (largura_janela - largura_imagen) // 2
    posicao_y = (altura_janela - altura_imagen) // 2

    lbl_imagem.place(x=posicao_x,y=posicao_y)

imagem = PhotoImage(file="imagens/genga")
lbl_imagem = ttk.Label(janela_principal, image=imagem)

janela_principal.bind("<Configure>", definir_imagens)
lbl_imagem.pack()
    

botao = tk.Button(janela_principal, text="Botao", command=abrir_segunda_janela)
botao.pack()

# janela_principal.bind("<Button-1>", lambda event: abrir_segunda_janela())


janela_principal.mainloop()



