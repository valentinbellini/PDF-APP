import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from .fts_encrypt import *

# Función para abrir la interfaz de "Encrypt File"
def open_encrypt_file():
    # Función para manejar la acción de encrypt file
    def on_encrypt():
        input_pdf = input_pdf_entry.get()
        if input_pdf:
            encrypt_file(input_pdf)
            messagebox.showinfo("Éxito", f"El archivo '{input_pdf}' ha sido encriptado.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    # Función para manejar la acción de eliminar encritpación
    def on_decrypt():
        input_pdf = input_pdf_entry.get()
        if input_pdf:
            decrypt_file(input_pdf)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")


    # Función para seleccionar un archivo PDF
    def select_file(entry):
        # Allow selection of both PDF and .encrypted files
        filetypes = [
            ("PDF files", "*.pdf"),
            ("Encrypted files", "*.encrypted"),
            ("All files", "*.*")  # Optional: to allow any file type
        ]

        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:  # Check if a file was selected
            entry.delete(0, tk.END)
            entry.insert(0, file_path)

    pdf_window = Toplevel()
    pdf_window.title("Encrypt PDF")
    pdf_window.geometry("250x200")

    # Crear los campos de entrada
    input_pdf_entry = tk.Entry(pdf_window, width=40)

    # Crear botones para las acciones
    tk.Label(pdf_window, text="Archivo PDF de entrada:").pack(pady=5)
    input_pdf_entry.pack(pady=5)
    tk.Button(pdf_window, text="Examinar", command=lambda: select_file(input_pdf_entry)).pack(pady=5)

    # Salto de linea de 10 px
    tk.Frame(pdf_window, height=10).pack()  

    # Botones de acción
    tk.Button(pdf_window, text="Encrypt PDF", command=on_encrypt).pack(pady=5)
    tk.Button(pdf_window, text="Decrypt PDF", command=on_decrypt).pack(pady=5)
