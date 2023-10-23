
import tkinter as tk
from tkinter import filedialog
import struct
import os

def pack_files(file_list, output_file):
    with open('list.txt', 'w', encoding='utf-8') as list_file:
        list_file.write("")

    with open(output_file, 'wb') as pak_file:
        list_file_offset = 0  # Inicialmente, a lista de arquivos está vazia

        for file_name in file_list:
            with open(file_name, 'rb') as input_file:
                file_data = input_file.read()
                pak_file.write(file_data)

            # Atualize o arquivo de lista (list.txt)
            with open('list.txt', 'a', encoding='utf-8') as list_file:
                file_names = os.path.basename(file_name)
                list_file.write(f"{file_names},{list_file_offset}\n")

            # Atualize o deslocamento para o próximo arquivo
            list_file_offset += len(file_data)

    # No final do arquivo de saída (out.pak), grave o arquivo list.txt
    with open(output_file, 'ab') as pak_file:
        with open('list.txt', 'rb') as list_file:
            list_data = list_file.read()
            pak_file.write(list_data)

    # Grave o deslocamento da lista no final do arquivo (out.pak)
    with open(output_file, 'ab') as pak_file:
        pak_file.seek(0, 2)
        pak_file.write(struct.pack('Q', list_file_offset))

def pack_files_gui():
    root = tk.Tk()
    root.title("Empacotar Arquivos")
    root.configure(bg="brown", width=800, height=600)  # Define a cor de 
    def browse_files():
        file_paths = filedialog.askopenfilenames(title="Selecione os arquivos para empacotar")
        file_list.delete(0, tk.END)
        for file_path in file_paths:
            file_list.insert(tk.END, file_path)

    def pack():
        file_paths = file_list.get(0, tk.END)
        output_file_path = output_file_entry.get()
        if file_paths and output_file_path:
            pack_files(file_paths, output_file_path)
            result_label.config(text="Arquivos empacotados com sucesso.")
        else:
            result_label.config(text="Por favor, selecione arquivos de entrada e um arquivo de saída.")

    file_list_label = tk.Label(root, text="Arquivos de entrada:")
    file_list = tk.Listbox(root, selectmode=tk.MULTIPLE, exportselection=0)
    browse_button = tk.Button(root, text="Selecionar Arquivos", command=browse_files)
    output_file_label = tk.Label(root, text="Arquivo de saída:")
    output_file_entry = tk.Entry(root)
    pack_button = tk.Button(root, text="Empacotar Arquivos", command=pack)
    result_label = tk.Label(root, text="")

    file_list_label.pack()
    file_list.pack()
    browse_button.pack()
    output_file_label.pack()
    output_file_entry.pack()
    pack_button.pack()
    result_label.pack()

    root.mainloop()

pack_files_gui()
