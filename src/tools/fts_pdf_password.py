from tkinter import messagebox
from PyPDF2 import PdfReader, PdfWriter
import logging

# Set up logging for the module
logger = logging.getLogger(__name__)  # Identifies the module for log messages


# === Error Handling ===
def handle_error(exception, user_message):
    """
    Handles errors centrally by logging and displaying messages.
    
    Parameters:
        exception (Exception): The exception object to log.
        user_message (str): The message to show to the user in the UI.
    """
    logger.error(f"{exception.__class__.__name__}: {exception}")
    messagebox.showerror("Error", user_message)


# === Decrypt and Remove Password ===
def decrypt_pdf(input_pdf, password):
    """
    Decrypts a password-protected PDF file.
    
    Parameters:
        input_pdf (str): Path to the PDF file to decrypt.
        password (str): The password for the PDF file.
    
    Returns:
        PdfReader, bool: The PdfReader object and whether the file was encrypted.
    """
    try:
        pdf_reader = PdfReader(input_pdf)
        if not pdf_reader.is_encrypted:
            messagebox.showinfo("Information", f"The file '{input_pdf}' is not password-protected.")
            return pdf_reader, False
        if not pdf_reader.decrypt(password):
            raise ValueError("Incorrect password")
        return pdf_reader, True
    except FileNotFoundError:
        handle_error(FileNotFoundError, f"The file '{input_pdf}' does not exist.")
    except ValueError as e:
        handle_error(e, str(e))
    except Exception as e:
        handle_error(e, f"Unknown error while unlocking: {e}")
    return None, False


def save_pdf(reader, output_pdf):
    """
    Saves a PDF file after decrypting it.
    
    Parameters:
        reader (PdfReader): A PdfReader object of the decrypted PDF.
        output_pdf (str): Path to save the new PDF file.
    """
    try:
        pdf_writer = PdfWriter()
        for page in reader.pages:
            pdf_writer.add_page(page)
        with open(output_pdf, "wb") as file:
            pdf_writer.write(file)
        messagebox.showinfo("Success", f"The file '{output_pdf}' has been saved without password protection.")
    except Exception as e:
        handle_error(e, f"Error saving the file: {e}")


def remove_password(input_pdf, output_pdf, password):
    """
    Removes the password protection from a PDF file.
    
    Parameters:
        input_pdf (str): Path to the password-protected PDF file.
        output_pdf (str): Path to save the unprotected PDF file.
        password (str): The password for the PDF file.
    """
    reader, was_encrypted = decrypt_pdf(input_pdf, password)
    if reader and was_encrypted:
        save_pdf(reader, output_pdf)


# === Password Protection ===
def protect_pdf(input_pdf, output_pdf, password):
    """
    Protects a PDF file by adding password encryption.
    
    Parameters:
        input_pdf (str): Path to the PDF file to protect.
        output_pdf (str): Path to save the encrypted PDF file.
        password (str): The password to encrypt the file with.
    """
    try:
        pdf_writer = PdfWriter()
        pdf_reader = PdfReader(input_pdf)

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        pdf_writer.encrypt(password)

        with open(output_pdf, "wb") as file:
            pdf_writer.write(file)

        messagebox.showinfo("Success", f"The file '{output_pdf}' has been protected with a password.")
    except FileNotFoundError:
        handle_error(FileNotFoundError, f"The file '{input_pdf}' does not exist.")
    except Exception as e:
        handle_error(e, f"Error protecting the file: {e}")


# === Protection Check ===
def check_protection(input_pdf):
    """
    Checks if a PDF file is password-protected.
    
    Parameters:
        input_pdf (str): Path to the PDF file to check.
    """
    try:
        pdf_reader = PdfReader(input_pdf)
        if pdf_reader.is_encrypted:
            messagebox.showinfo("Information", f"The file '{input_pdf}' is password-protected.")
        else:
            messagebox.showinfo("Information", f"The file '{input_pdf}' is not password-protected.")
    except FileNotFoundError:
        handle_error(FileNotFoundError, f"The file '{input_pdf}' does not exist.")
    except Exception as e:
        handle_error(e, f"Error checking protection for the file: {e}")
