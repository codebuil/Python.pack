import sys
import struct

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
                list_file.write(f"{file_name},{list_file_offset}\n")

            # Atualize o deslocamento para o próximo arquivo
            list_file_offset += len(file_data)

        # No final do arquivo de saída (out.pak), grave o arquivo list.txt
    with open(output_file, 'a', encoding='utf-8') as pak_file:
        with open('list.txt', 'r', encoding='utf-8') as list_file:
            list_data = list_file.read()
            pak_file.write(list_data)

        # Grave o deslocamento da lista no final do arquivo (out.pak)
    with open(output_file, 'ab') as pak_file:
        pak_file.seek(0, 2)
        pak_file.write(struct.pack('Q', list_file_offset))

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")
    if len(sys.argv) < 3:
        print("Uso: python pack_files.py <output_file> <file1> <file2> ...")
    else:
        output_file = sys.argv[1]
        file_list = sys.argv[2:]
        pack_files(file_list, output_file)

