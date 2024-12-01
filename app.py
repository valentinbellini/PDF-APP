import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from PyPDF2 import PdfReader, PdfWriter
from tk_window_pdf_pass import *


# Funciones para otras aplicaciones (puedes personalizar estas interfaces)
def open_file_cleaner():
    cleaner_window = Toplevel()
    cleaner_window.title("File Cleaner")
    cleaner_window.geometry("400x200")
    tk.Label(cleaner_window, text="Esta es la interfaz del limpiador de archivos").pack(pady=20)

def open_file_encrypt():
    encrypt_window = Toplevel()
    encrypt_window.title("File Encrypt")
    encrypt_window.geometry("400x200")
    tk.Label(encrypt_window, text="Esta es la interfaz del cifrado de archivos").pack(pady=20)

def open_free_memory():
    memory_window = Toplevel()
    memory_window.title("Free Memory")
    memory_window.geometry("400x200")
    tk.Label(memory_window, text="Esta es la interfaz para liberar memoria").pack(pady=20)




# Crear la ventana principal
root = tk.Tk()
root.title("Aplicaciones Utilitarias")
root.geometry("300x300")

# Crear botones en el menú principal
tk.Button(root, text="PDF Lock", command=open_pdf_lock, width=20, height=2).pack(pady=10)
tk.Button(root, text="File Cleaner", command=open_file_cleaner, width=20, height=2).pack(pady=10)
tk.Button(root, text="File Encrypt", command=open_file_encrypt, width=20, height=2).pack(pady=10)
tk.Button(root, text="Free Memory", command=open_free_memory, width=20, height=2).pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()