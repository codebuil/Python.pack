import sys

def format_string_to_length(s, length):
    if len(s) < length:
        s = s.ljust(length, '\0')
    elif len(s) > length:
        s = s[:length]
    return s

def replace_first_char_in_file(input_filename, output_filename, search_string, replacement_string):
    with open(input_filename, 'rb') as input_file:
        file_content = input_file.read()

        # Procura pela string '1' no conteúdo do arquivo
        
        modified_replacement = format_string_to_length(replacement_string, len(search_string))
        modified_content = file_content.replace(search_string.encode(), modified_replacement.encode())
        
        with open(output_filename, 'wb') as output_file:
            output_file.write(modified_content)
        
if __name__ == "__main__":
    print("\x1bc\x1b[43;37m")
    if len(sys.argv) != 5:
        print("Uso: python script.py <ficheiro_de_entrada> <ficheiro_de_saida> <string_1> <string_2>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        search_string = sys.argv[3]
        replacement_string = sys.argv[4]
        replace_first_char_in_file(input_file, output_file, search_string, replacement_string)

