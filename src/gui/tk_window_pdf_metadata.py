import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter.ttk import Combobox
from ..tools.fts_pdf_metadata import read_metadata, add_metadata

# Function to open the "Metadata Management" interface
def open_pdf_metadata():
    # Function to open the "Metadata Management" interface
    def on_read_metadata():
        input_pdf = input_pdf_entry.get()
        if input_pdf:
            metadata_display.delete(1.0, tk.END)
            metadata_display.insert(tk.END, f"Metadatos del archivo: {input_pdf}\n\n")
            metadata = read_metadata(input_pdf)
            metadata_display.insert(tk.END, metadata)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo PDF.")

    # Function to handle the action of reading metadata
    def on_add_metadata():
        input_pdf = input_pdf_entry.get()
        output_pdf = output_pdf_entry.get()
        key = key_combobox.get()
        value = value_entry.get()
        if input_pdf and output_pdf and key and value:
            result = add_metadata(input_pdf, output_pdf, key, value)
            messagebox.showinfo("Resultado", result)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    # Function to select a PDF file
    def select_file(entry):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    pdf_window = Toplevel()
    pdf_window.title("Gestión de Metadatos")
    pdf_window.geometry("600x500")

    # Create the input fields
    input_pdf_entry = tk.Entry(pdf_window, width=40)
    output_pdf_entry = tk.Entry(pdf_window, width=40)
    value_entry = tk.Entry(pdf_window, width=40)

    # List of typical metadata fields
    metadata_fields = [
        "/Title", "/Author", "/Subject", "/Keywords",
        "/Creator", "/Producer", "/CreationDate", "/ModDate"
    ]

    # Create a combobox to select the metadata key
    key_combobox = Combobox(pdf_window, values=metadata_fields, state="readonly", width=37)
    key_combobox.set("Seleccionar campo")

    # Create buttons and labels
    tk.Label(pdf_window, text="Archivo PDF de entrada:").pack(pady=5)
    input_pdf_entry.pack(pady=5)
    tk.Button(pdf_window, text="Seleccionar", command=lambda: select_file(input_pdf_entry)).pack(pady=5)

    tk.Label(pdf_window, text="Archivo PDF de salida:").pack(pady=5)
    output_pdf_entry.pack(pady=5)
    tk.Button(pdf_window, text="Seleccionar", command=lambda: select_file(output_pdf_entry)).pack(pady=5)

    tk.Label(pdf_window, text="Clave del Metadato:").pack(pady=5)
    key_combobox.pack(pady=5)

    tk.Label(pdf_window, text="Valor del Metadato:").pack(pady=5)
    value_entry.pack(pady=5)

    # Action buttons
    tk.Button(pdf_window, text="Leer Metadatos", command=on_read_metadata).pack(pady=10)
    tk.Button(pdf_window, text="Agregar/Modificar Metadato", command=on_add_metadata).pack(pady=10)

    # Text box to display metadata
    metadata_display = tk.Text(pdf_window, wrap="word", height=20, width=70)
    metadata_display.pack(pady=10)


