from pikepdf import Pdf
from src.tools.utils import handle_error
from .utils import get_logger, handle_error

logger = get_logger("pdf_metadata")  # Create a logger for this specific module

# Function to read PDF metadata
def read_metadata(input_pdf):
    """
    Reads the metadata of a PDF file.

    Parameters:
        input_pdf (str): Path to the input PDF file.

    Returns:
        str: Metadata as a formatted string or an error message.
    """
    try:
        pdf = Pdf.open(input_pdf)
        metadata = pdf.docinfo
        metadata_info = []
        if metadata:
            # return "\n".join(f"{key}: {value}" for key, value in metadata.items())
            for key, value in metadata.items():
                metadata_info.append(f"{key}: {value}")
        else:
            # return "No metadata found."
            metadata_info.append("No se encontraron metadatos.")
        return "\n".join(metadata_info)
    except Exception as e:
        handle_error(e, f"Error reading metadata for '{input_pdf}'")
        return None

# Function to add or modify a metadata in the PDF
def add_metadata(input_pdf, output_pdf, key, value):
    """
    Adds or modifies metadata in a PDF file.

    Parameters:
        input_pdf (str): Path to the input PDF file.
        output_pdf (str): Path to save the updated PDF file.
        key (str): Metadata key to add or modify.
        value (str): Metadata value to set.

    Returns:
        str: Success or error message.
    """
    try:
        with Pdf.open(input_pdf, allow_overwriting_input=True) as pdf:
            pdf.docinfo[key] = value
            pdf.save(output_pdf)
        return f"Metadato '{key}' agregado/modificado con éxito en '{output_pdf}'."
    except Exception as e:
        handle_error(e, f"Error updating metadata for '{input_pdf}'")
        return None
