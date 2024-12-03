import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from .fts_encrypt import *

# Function to open the interface of "Encrypt File"
def open_encrypt_file():
    # Function to handle the encrypt file action
    def on_encrypt():
        input_pdf = input_pdf_entry.get()
        if input_pdf:
            encrypt_file(input_pdf)
            messagebox.showinfo("Éxito", f"El archivo '{input_pdf}' ha sido encriptado.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    # Function to handle the action of deleting encryption
    def on_decrypt():
        input_pdf = input_pdf_entry.get()
        if input_pdf:
            decrypt_file(input_pdf)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")


    # Function to select a PDF file
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

    # Create the input fields
    input_pdf_entry = tk.Entry(pdf_window, width=40)

    # Create buttons for the actions
    tk.Label(pdf_window, text="Archivo PDF de entrada:").pack(pady=5)
    input_pdf_entry.pack(pady=5)
    tk.Button(pdf_window, text="Examinar", command=lambda: select_file(input_pdf_entry)).pack(pady=5)

    # 10px line break (hop)
    tk.Frame(pdf_window, height=10).pack()  

    # Action Buttons
    tk.Button(pdf_window, text="Encrypt PDF", command=on_encrypt).pack(pady=5)
    tk.Button(pdf_window, text="Decrypt PDF", command=on_decrypt).pack(pady=5)
