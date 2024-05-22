

def create_file(txt, file_name):

    try:
        with open("files/"+file_name, 'w', encoding='utf-8') as archivo:
            archivo.write(txt)
        print(f"Texto guardado en {file_name}")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

def create_file_from_list(txt,file_name):

    try:
        with open("files/"+file_name, 'w') as file:
            for item in txt:
                file.write(f"{item}\n")
        print(f"Texto guardado en {file_name}")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")