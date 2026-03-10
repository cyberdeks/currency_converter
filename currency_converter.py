import requests
import tkinter as tk
from tkinter import messagebox

def converter_moeda():

    base = moeda_base_entry.get().upper()
    target = moeda_target_entry.get().upper()
    amount = float(moeda_amount_entry.get())

    url = f"https://api.exchangerate-api.com/v4/latest/{base}"

    resposta = requests.get(url)
    dados = resposta.json()

    try:
        cotacao = dados["rates"][target]
        resultado = amount * cotacao

        messagebox.showinfo("Conversion", f"{amount} {base} = {resultado:.2f} {target}")
       
    except:
        messagebox.showerror("Error", "Invalid currency code!")

janela = tk.Tk()
janela.title("Currency Converter")

largura = 300
altura = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = int(largura_tela / 2 - largura / 2)
pos_y = int(altura_tela / 2 - altura / 2)
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

label_moeda_base = tk.Label(janela, text="Base Currency:")
label_moeda_base.pack(pady=10)
moeda_base_entry = tk.Entry(janela, width = 5)
moeda_base_entry.pack(pady=5)

label_moeda_target = tk.Label(janela, text="Target Currency:")
label_moeda_target.pack(pady=10)
moeda_target_entry = tk.Entry(janela, width = 5)
moeda_target_entry.pack(pady=5)

label_moeda_amount = tk.Label(janela, text="Amount:")
label_moeda_amount.pack(pady=10)
moeda_amount_entry = tk.Entry(janela, width = 13)
moeda_amount_entry.pack(pady=5)

botao_converter = tk.Button(janela, text="Convert", command=converter_moeda, width=15)
botao_converter.pack(pady=20)

janela.mainloop()