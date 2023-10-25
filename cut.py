
import sys

def copy_file_segment(input_filename, output_filename, start_offset, size):
    try:
        with open(input_filename, 'rb') as input_file, open(output_filename, 'wb') as output_file:
            input_file.seek(start_offset)
            data = input_file.read(size)
            output_file.write(data)
        print(f"Copiado {size} bytes do arquivo de entrada para o arquivo de saída.")
    except FileNotFoundError:
        print("O arquivo de entrada não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")
    if len(sys.argv) != 5:
        print("Uso: python copy_file_segment.py <arquivo_de_entrada> <arquivo_de_saída> <offset> <tamanho>")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        start_offset = int(sys.argv[3])
        size = int(sys.argv[4])
        copy_file_segment(input_filename, output_filename, start_offset, size)
