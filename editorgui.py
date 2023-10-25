import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

app = tk.Tk()
app.title("Editor de Texto Simples")
app.configure(bg="brown", width=800, height=600)  # Define a cor de 

text = tk.Text(app, wrap=tk.WORD)
text.pack()

open_button = tk.Button(app, text="Abrir Arquivo", command=open_file)
save_button = tk.Button(app, text="Salvar Arquivo", command=save_file)

open_button.pack()
save_button.pack()

app.mainloop()

