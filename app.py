from tk_window_pdf_pass import *
from tk_window_encrypt import *
from tk_window_pdf_metadata import *


# Funciones para otras aplicaciones (puedes personalizar estas interfaces)
def open_file_cleaner():
    cleaner_window = Toplevel()
    cleaner_window.title("File Cleaner")
    cleaner_window.geometry("400x200")
    tk.Label(cleaner_window, text="Esta es la interfaz del limpiador de archivos").pack(pady=20)


# Crear la ventana principal
root = tk.Tk()
root.title("Aplicaciones Utilitarias")
root.geometry("300x200")

# Crear botones en el menú principal
tk.Button(root, text="PDF Password", command=open_pdf_lock, width=20, height=2).pack(pady=10)
tk.Button(root, text="File Encrypt", command=open_encrypt_file, width=20, height=2).pack(pady=10)
tk.Button(root, text="PDF Metadata", command=open_pdf_metadata, width=20, height=2).pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()