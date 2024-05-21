

def create_file(txt, file_name):

    try:
        with open("files/"+file_name, 'w', encoding='utf-8') as archivo:
            archivo.write(txt)
        print(f"Texto guardado en {file_name}")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")
