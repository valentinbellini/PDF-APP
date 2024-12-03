from tkinter import messagebox
from PyPDF2 import PdfReader, PdfWriter


# Feature to protect a PDF file with a password
def protect_pdf(input_pdf, output_pdf, password):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_pdf)

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(password)

    with open(output_pdf, "wb") as file:
        pdf_writer.write(file)
    messagebox.showinfo("Éxito", f"El archivo '{output_pdf}' ha sido protegido con contraseña.")

# Feature to check if a PDF file is already protected
def check_protection(input_pdf):
    pdf_reader = PdfReader(input_pdf)
    if pdf_reader.is_encrypted:
        messagebox.showinfo("Información", f"El archivo '{input_pdf}' ya está protegido.")
    else:
        messagebox.showinfo("Información", f"El archivo '{input_pdf}' no tiene protección.")

# Feature to remove password from a protected PDF file
def remove_password(input_pdf, output_pdf, password):
    pdf_reader = PdfReader(input_pdf)

    if pdf_reader.is_encrypted:
        try:
            # Try to decrypt the PDF file with the password provided
            decryption_result = pdf_reader.decrypt(password)

            # If the password is incorrect, the result of decrypt() is 0
            # [PYPDF2] TODO: raise Exception for wrong password - waiting update
            if decryption_result == 0:
                messagebox.showerror("Error", "Contraseña incorrecta.")
                return

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

