from pikepdf import Pdf

# Función para leer los metadatos del PDF
def read_metadata(input_pdf):
    try:
        pdf = Pdf.open(input_pdf)
        metadata = pdf.docinfo
        metadata_info = []
        
        if metadata:
            for key, value in metadata.items():
                metadata_info.append(f"{key}: {value}")
        else:
            metadata_info.append("No se encontraron metadatos.")
        
        return "\n".join(metadata_info)
    except Exception as e:
        return f"Error al leer los metadatos: {e}"

# Función para agregar o modificar un metadato en el PDF
def add_metadata(input_pdf, output_pdf, key, value):
    try:
        with Pdf.open(input_pdf, allow_overwriting_input=True) as pdf:
            pdf.docinfo[key] = value
            pdf.save(output_pdf)
        return f"Metadato '{key}' agregado/modificado con éxito en '{output_pdf}'."
    except Exception as e:
        return f"Error al agregar/modificar metadato: {e}"
