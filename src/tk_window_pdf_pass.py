import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from .fts_pdf_password import *

# Function to open the "PDF Lock" interface
def open_pdf_lock():
    # Function to handle the action of protecting PDF
    def on_protect():
        input_pdf = input_pdf_entry.get()
        output_pdf = input_pdf_entry.get() # output_pdf_entry.get()
        password = password_entry.get()
        if input_pdf and output_pdf and password:
            protect_pdf(input_pdf, output_pdf, password)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    # Function to handle the action of checking protection
    def on_check():
        input_pdf = input_pdf_entry.get()
        if input_pdf:
            check_protection(input_pdf)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo PDF.")

    # Function to handle the action of deleting password
    def on_remove():
        input_pdf = input_pdf_entry.get()
        output_pdf = input_pdf_entry.get() # output_pdf_entry.get()
        password = password_entry.get()
        if input_pdf and output_pdf and password:
            remove_password(input_pdf, output_pdf, password)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    # Function to select a PDF file
    def select_file(entry):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    pdf_window = Toplevel()
    pdf_window.title("Protección de PDF")
    pdf_window.geometry("400x300")

    # Create the input fields
    input_pdf_entry = tk.Entry(pdf_window, width=40)
    # output_pdf_entry = tk.Entry(pdf_window, width=40)
    password_entry = tk.Entry(pdf_window, show="*", width=40)

    # Create buttons for the actions
    tk.Label(pdf_window, text="Archivo PDF de entrada:").pack(pady=5)
    input_pdf_entry.pack(pady=5)
    tk.Button(pdf_window, text="Examinar", command=lambda: select_file(input_pdf_entry)).pack(pady=5)

    # tk.Label(pdf_window, text="Archivo PDF de salida:").pack(pady=5)
    # output_pdf_entry.pack(pady=5)
    # tk.Button(pdf_window, text="Examinar", command=lambda: select_file(output_pdf_entry)).pack(pady=5)

    tk.Label(pdf_window, text="Contraseña:").pack(pady=5)
    password_entry.pack(pady=5)

     # 10px break line (hop)
    tk.Frame(pdf_window, height=20).pack()  
    
    # Action Buttons
    tk.Button(pdf_window, text="Proteger PDF", command=on_protect).pack(pady=5)
    tk.Button(pdf_window, text="Verificar Protección", command=on_check).pack(pady=5)
    tk.Button(pdf_window, text="Eliminar Contraseña", command=on_remove).pack(pady=5)
