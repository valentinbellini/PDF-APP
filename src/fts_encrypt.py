from cryptography.fernet import Fernet
from tkinter import messagebox
from pathlib import Path
import os

# Path where .keys file 
KEYS_DIR = Path(__file__).parent / "keys"
KEYS_DIR.mkdir(exist_ok=True)  # Create folder if doesn't exist

# Function to generate and save an unique key for each file
def generate_and_save_key(file_name):
    key = Fernet.generate_key()  # Generar una clave única
    key_file_path = KEYS_DIR / f"{file_name}.key"  # Guardar clave en src/encrypt_files/keys/<nombre_archivo>.key
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)  # Guardar la clave en un archivo
    return key

# Function to load the key of the file
def load_key(file_name):
    key_file_path = KEYS_DIR / f"{file_name}.key"  # Buscar clave en src/encrypt_files/keys/<nombre_archivo>.key
    if not key_file_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de clave: {key_file_path}")
    with open(key_file_path, "rb") as key_file:
        return key_file.read()

# Function to encrypt a file
def encrypt_file(file_path):
    file_path = Path(file_path)  # Convert into a Path Object
    if not file_path.exists():
        print(f"El archivo {file_path} no existe.")
        return

    # Generate and save key
    key = generate_and_save_key(file_path.stem)  # Save key with the document's name
    fernet = Fernet(key)

    # Read and encrypt the file's content
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)

    # Save the encrypt file
    encrypted_file_path = file_path.with_suffix(".encrypted")
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    # print(f"Archivo encriptado guardado como: {encrypted_file_path}")
    # print(f"Clave guardada en: {file_path.stem}.key")
    
    # Ask the user to eliminate the original document
    if messagebox.askyesno("Eliminar archivo original", f"¿Desea eliminar el archivo original '{file_path}'?"):
        os.remove(file_path)
        print(f"Archivo original '{file_path}' eliminado.")

# File Decryption Function
def decrypt_file(encrypted_file_path):
    encrypted_file_path = Path(encrypted_file_path)  # Convert into a Path Object
    if not encrypted_file_path.exists():
        print(f"El archivo {encrypted_file_path} no existe.")
        return

    try: 
        # Load corresponding key
        key = load_key(encrypted_file_path.stem)  # We assume <archivo> that .encrypted uses <archivo>.key
        fernet = Fernet(key)

        # Read and decrypt file contents
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = fernet.decrypt(encrypted_data)

        # save the decrypt file
        original_file_path = encrypted_file_path.with_suffix(".decrypted")
        with open(original_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
            
        # Ask the user if they want to delete the encrypted file
        if messagebox.askyesno("Eliminar archivo encriptado", f"¿Desea eliminar el archivo encriptado '{encrypted_file_path}'?"):
            os.remove(encrypted_file_path)
            print(f"Archivo encriptado '{encrypted_file_path}' eliminado.")
            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption. Be sure the file extension is .encrypted")

    # print(f"Archivo desencriptado guardado como: {original_file_path}")
    
    
