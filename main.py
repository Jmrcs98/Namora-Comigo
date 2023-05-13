import random
import tkinter as tk
from tkinter import messagebox

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x350")
        self.master.title("Quer namorar comigo?")
        self.create_widgets()
        
    def create_widgets(self):
        self.title = tk.Label(self.master, text="Quer namorar comigo?", font=("Arial", 20), background="pink")
        self.title.place(relx=0.5, rely=0.3, anchor="center")
        self.title.config(fg="red")

        self.btn_sim = tk.Button(self.master, text="Sim", command=self.mostrar_mensagem)
        self.btn_sim.grid(row=1, column=0, padx=50, pady=160)

        self.btn_nao = tk.Button(self.master, text="Não")
        self.btn_nao.grid(row=1, column=1, padx=50, pady=160)
        self.btn_nao.bind("<Enter>", self.mover_botao_nao)

    def mover_botao_nao(self, event):
        x = random.randint(0, self.master.winfo_width() - self.btn_nao.winfo_width())
        y = random.randint(0, self.master.winfo_height() - self.btn_nao.winfo_height())
        self.btn_nao.place(x=x, y=y)

    def mostrar_mensagem(self):
        messagebox.showinfo("Melhor escolha", "Parabéns! Você fez a melhor escolha.")
        self.coracao = tk.PhotoImage(file="coracao.png")
        self.coracao_label = tk.Label(self.master, image=self.coracao)
        self.coracao_label.image = self.coracao
        self.coracao_label.place(relx=0.5, rely=0.5, anchor="center")
        self.btn_sim.grid_forget()
        self.btn_nao.grid_forget()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()