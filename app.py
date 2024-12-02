from src.tk_window_pdf_pass import *
from src.tk_window_encrypt import *
from src.tk_window_pdf_metadata import *
import webbrowser

# Función para abrir el enlace en el navegador
def open_link(event):
    webbrowser.open("https://github.com/valentinbellini/PDF-APP")
    
    
# Crear la ventana principal
root = tk.Tk()
root.title("Also PDF V1.1")
root.geometry("300x250")

# Crear botones en el menú principal
tk.Button(root, text="PDF Password", command=open_pdf_lock, width=20, height=2).pack(pady=10)
tk.Button(root, text="File Encrypt", command=open_encrypt_file, width=20, height=2).pack(pady=10)
tk.Button(root, text="PDF Metadata", command=open_pdf_metadata, width=20, height=2).pack(pady=10)


# Crear un Label para mostrar el texto del hipervínculo
link = tk.Label(root, text="https://github.com/valentinbellini/PDF-APP", fg="blue", cursor="hand2")
link.pack(pady=20)
# Asociar el clic del ratón con la función para abrir el enlace
link.bind("<Button-1>", open_link)

# Iniciar el bucle principal de la aplicación
root.mainloop()