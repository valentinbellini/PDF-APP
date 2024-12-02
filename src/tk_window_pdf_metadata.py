import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter.ttk import Combobox
from .fts_pdf_metadata import read_metadata, add_metadata

# Función para abrir la interfaz de "Gestión de Metadatos"
def open_pdf_metadata():
    # Función para manejar la acción de leer metadatos
    def on_read_metadata():
        input_pdf = input_pdf_entry.get()
        if input_pdf:
            metadata_display.delete(1.0, tk.END)
            metadata_display.insert(tk.END, f"Metadatos del archivo: {input_pdf}\n\n")
            metadata = read_metadata(input_pdf)
            metadata_display.insert(tk.END, metadata)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo PDF.")

    # Función para manejar la acción de agregar un metadato
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

    # Función para seleccionar un archivo PDF
    def select_file(entry):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    pdf_window = Toplevel()
    pdf_window.title("Gestión de Metadatos")
    pdf_window.geometry("600x500")

    # Crear los campos de entrada
    input_pdf_entry = tk.Entry(pdf_window, width=40)
    output_pdf_entry = tk.Entry(pdf_window, width=40)
    value_entry = tk.Entry(pdf_window, width=40)

    # Lista de campos típicos de metadatos
    metadata_fields = [
        "/Title", "/Author", "/Subject", "/Keywords",
        "/Creator", "/Producer", "/CreationDate", "/ModDate"
    ]

    # Crear un combobox para seleccionar la clave del metadato
    key_combobox = Combobox(pdf_window, values=metadata_fields, state="readonly", width=37)
    key_combobox.set("Seleccionar campo")

    # Crear botones y etiquetas
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

    # Botones de acción
    tk.Button(pdf_window, text="Leer Metadatos", command=on_read_metadata).pack(pady=10)
    tk.Button(pdf_window, text="Agregar/Modificar Metadato", command=on_add_metadata).pack(pady=10)

    # Caja de texto para mostrar los metadatos
    metadata_display = tk.Text(pdf_window, wrap="word", height=20, width=70)
    metadata_display.pack(pady=10)


