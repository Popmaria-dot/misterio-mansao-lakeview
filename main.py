import tkinter as tk

janela = tk.Tk()

janela.title("O Mistério da Mansão Lakeview")
janela.geometry("800x600")
janela.configure(bg="#080808")

# Inventário do jogador
inventario = []
texto_carta = (
    "Quando o relógio silenciar, não confie nas horas."
    "\nUm inocente teme ser acusado, um culpado teme ser descoberto."
    "\nA verdade não desaparece, apenas muda de lugar."
    "\nDebaixo dos olhos que nunca piscam, deixei aquilo que ele procurava."
    "\nRastros podem ser criados para contar uma história que nunca aconteceu."
    "\nObserve com atenção. Nesta casa, até os mortos continuam olhando."
)

# Áreas principais da janela

frame_titulo = tk.Frame(janela, bg="#080808")
frame_titulo.pack()


frame_inventario = tk.Frame(janela, bg="#080808")
frame_inventario.pack(anchor="e", pady=20)

titulo = tk.Label(
    frame_titulo,
    text="O MISTÉRIO DA MANSÃO LAKEVIEW",
    bg="#080808",
    fg="white",
    font=("Georgia", 20, "bold")
)
titulo.pack(pady=20)

frame_historia = tk.Frame(janela, bg="#080808")
frame_historia.pack()

investigador = tk.Label(
    frame_historia,
    text="Investigador: Sr. S",
    bg="#080808",
    fg="white",
    font=("Arial", 14)

)
investigador.pack(pady=10)

introducao = tk.Label(
    frame_historia,
    text="A chuva cai violentamente sobre a mansão Lakeview...",
    bg=("#080808"),
    fg="white",
    font=("Arial", 12)

)
introducao.pack(pady=10)


frame_opcoes = tk.Frame(janela)
frame_opcoes.pack()


def entrar_mansao():
    introducao.config(text="O Sr. S entrou na Mansão Lakeview.")
    botao_entrar.pack_forget()
    botao_sair.pack_forget()
    botao_sala.pack(pady=10)


botao_entrar = tk.Button(
    frame_opcoes,
    text="Entrar na Mansão",
    command=entrar_mansao,
    bg=("#FAFAFA"),
    fg="black",
    activebackground="#030303",
    activeforeground="white",
    font=("Georgia", 12, "bold"),
    padx=20,
    pady=2,
    relief="flat",
    borderwidth=0
)
botao_entrar.pack(pady=10)


def sair_mansao():
    introducao.config(text="O Sr. S decidiu ir embora.")
    botao_sair.pack_forget()
    botao_entrar.pack_forget()
    botao_voltar.pack(pady=10)


botao_sair = tk.Button(
    frame_opcoes,
    text="Ir Embora",
    command=sair_mansao,
    bg=("#FAFAFA"),
    fg="black",
    activebackground="#030303",
    activeforeground="white",
    font=("Georgia", 12, "bold"),
    padx=20,
    pady=2,
    relief="flat",
    borderwidth=0
)
botao_sair.pack(pady=10)


def voltar():
    introducao.config(
        text="A chuva cai violentamente sobre a Mansão Lakeview...")
    botao_voltar.pack_forget()
    botao_entrar.pack(pady=10)
    botao_sair.pack(pady=10)


botao_voltar = tk.Button(
    frame_opcoes,
    text="Voltar para a mansão",
    command=voltar,
    bg=("#FAFAFA"),
    fg="black",
    activebackground="#030303",
    activeforeground="white",
    font=("Georgia", 12, "bold"),
    padx=20,
    pady=2,
    relief="flat",
    borderwidth=0
)


def examinar_sala():
    introducao.config(
        text="O Sr. S examina cuidadosamente a sala."
        "\nA sala principal da Mansão Lakeview é grande e pouco iluminada."
        "\nA chuva bate contra as janelas, enquanto um antigo relógio de parede"
        "\nmarca o tempo em intervalos irregulares.\n"
        "\nSobre uma mesa há uma carta."
        "\nPerto da lareira, há um quadro antigo."
        "\nNo chão, próximo á janela, há uma marca de lama"

    )

    if "Carta Misteriosa" not in inventario:
        botao_carta.pack(pady=10)
        botao_sala.pack_forget()


botao_sala = tk.Button(
    frame_opcoes,
    text="Examinar a sala",
    command=examinar_sala,
    bg=("#FAFAFA"),
    fg="black",
    activebackground="#030303",
    activeforeground="white",
    font=("Georgia", 12, "bold"),
    padx=20,
    pady=2,
    relief="flat",
    borderwidth=0
)


def examinar_carta():
    introducao.config(
        text=texto_carta
    )

    botao_carta.pack_forget()
    botao_guardar.pack(pady=10)


botao_carta = tk.Button(
    frame_opcoes,
    text="Examinar a carta",
    command=examinar_carta,
    bg=("#FAFAFA"),
    fg="black",
    activebackground="#030303",
    activeforeground="white",
    font=("Georgia", 12, "bold"),
    padx=20,
    pady=2,
    relief="flat",
    borderwidth=0
)


def guardar_carta():
    if "Carta Misteriosa" not in inventario:
        inventario.append("Carta Misteriosa")
        introducao.config(
            text="O Sr. S dobra cuidadosamente a carta"
            " e a guarda no bolso de seu casaco."

        )
        botao_guardar.pack_forget()
        botao_sala.config(text="Continuar investigando a sala")
        botao_sala.pack(pady=10)


def abrir_inventario():
    if "Carta Misteriosa" in inventario:
        mensagem_inventario.config(text=texto_carta)
    else:
        mensagem_inventario.config(text="Inventário está vazio.")

    mensagem_inventario.pack(pady=10)

    botao_inventario.config(
        text="Fechar Inventário",
        command=fechar_inventario

    )


def fechar_inventario():
    mensagem_inventario.pack_forget()

    botao_inventario.config(
        text="Abrir Inventário",
        command=abrir_inventario
    )


botao_guardar = tk.Button(
    frame_opcoes,
    text="Guardar a carta",
    command=guardar_carta,
    bg=("#FAFAFA"),
    fg="black",
    activebackground="#030303",
    activeforeground="white",
    font=("Georgia", 12, "bold"),
    padx=20,
    pady=2,
    relief="flat",
    borderwidth=0
)

botao_inventario = tk.Button(
    frame_inventario,
    text="Inventário",
    command=abrir_inventario,
    bg=("#FAFAFA"),
    fg="black",
    font=("Georgia", 11, "bold"),
    padx=15,
    pady=5,
    relief="flat",
    borderwidth=0
)


mensagem_inventario = tk.Label(
    frame_inventario,
    text="",
    bg="#080808",
    fg="white",
    font=("Arial", 11),
    wraplength=650,
    justify="left"
)

botao_inventario.pack(pady=5)


janela.mainloop()
