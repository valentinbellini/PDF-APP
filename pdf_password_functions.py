import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter



# Función para proteger un archivo PDF con una contraseña
def protect_pdf(input_pdf, output_pdf, password):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_pdf)

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(password)

    with open(output_pdf, "wb") as file:
        pdf_writer.write(file)
    messagebox.showinfo("Éxito", f"El archivo '{output_pdf}' ha sido protegido con contraseña.")

# Función para verificar si un archivo PDF ya está protegido
def check_protection(input_pdf):
    pdf_reader = PdfReader(input_pdf)
    if pdf_reader.is_encrypted:
        messagebox.showinfo("Información", f"El archivo '{input_pdf}' ya está protegido.")
    else:
        messagebox.showinfo("Información", f"El archivo '{input_pdf}' no tiene protección.")

# Función para eliminar la contraseña de un archivo PDF protegido
def remove_password(input_pdf, output_pdf, password):
    pdf_reader = PdfReader(input_pdf)

    if pdf_reader.is_encrypted:
        try:
            pdf_reader.decrypt(password)
            messagebox.showinfo("Información", "Contraseña correcta. Eliminando protección...")
        except Exception as e:
            messagebox.showerror("Error", f"Error al desbloquear el archivo: {e}")
            return
    else:
        messagebox.showinfo("Información", f"El archivo '{input_pdf}' no tiene protección.")
        return

    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output_pdf, "wb") as file:
        pdf_writer.write(file)

    messagebox.showinfo("Éxito", f"El archivo '{output_pdf}' ha sido guardado sin protección.")



