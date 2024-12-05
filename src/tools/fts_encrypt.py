from cryptography.fernet import Fernet
from tkinter import messagebox
from pathlib import Path
import os
from .utils import get_logger, handle_error

logger = get_logger("file_encrypt")  # Create a logger for this specific module

# Path where .keys file 
KEYS_DIR = Path(__file__).parent / "keys"
KEYS_DIR.mkdir(exist_ok=True)  # Create folder if doesn't exist

# Function to generate and save an unique key for each file
def generate_and_save_key(file_name):
    """
    Generates and saves a unique encryption key for a file.

    Parameters:
        file_name (str): Name of the file to associate with the key.

    Returns:
        bytes: Generated encryption key.
    """
    try:
        key = Fernet.generate_key()
        key_file_path = KEYS_DIR / f"{file_name}.key"
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)
        return key
    except Exception as e:
        handle_error(e, "Error generating encryption key.")
        return None

# Function to load the key of the file
def load_key(file_name):
    """
    Loads the encryption key for a given file.

    Parameters:
        file_name (str): Name of the file whose key is to be loaded.

    Returns:
        bytes: The encryption key.
    """
    try:
        key_file_path = KEYS_DIR / f"{file_name}.key"
        if not key_file_path.exists():
            raise FileNotFoundError(f"Key file not found for '{file_name}'")
        with open(key_file_path, "rb") as key_file:
            return key_file.read()
    except Exception as e:
        handle_error(e, f"Error loading key for '{file_name}'.")
        return None

# Function to encrypt a file
def encrypt_file(file_path):
    """
    Encrypts a file and saves the encrypted version.

    Parameters:
        file_path (str): Path to the file to encrypt.
    """
    file_path = Path(file_path)  # Convert into a Path Object
    if not file_path.exists():
        messagebox.showerror("Error", f"The file '{file_path}' does not exist.")
        return

    try:
        key = generate_and_save_key(file_path.stem)
        if not key:
            return
        fernet = Fernet(key)
        
        # Read and encrypt the file's content
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)

        # Save the encrypt file
        encrypted_file_path = file_path.with_suffix(".encrypted")
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        if messagebox.askyesno("Delete Original File", f"Do you want to delete the original file '{file_path}'?"):
            os.remove(file_path)
            messagebox.showinfo("Success", f"Original file '{file_path}' deleted.")
    except Exception as e:
        handle_error(e, f"Error encrypting file '{file_path}'.")
    
# File Decryption Function
def decrypt_file(encrypted_file_path):
    """
    Decrypts an encrypted file and saves the decrypted version.

    Parameters:
        encrypted_file_path (str): Path to the encrypted file.
    """
    encrypted_file_path = Path(encrypted_file_path)  # Convert into a Path Object
    if not encrypted_file_path.exists():
        messagebox.showerror("Error", f"The file '{encrypted_file_path}' does not exist.")
        return
    try: 
        # Load corresponding key
        key = load_key(encrypted_file_path.stem)  # We assume <archivo> that .encrypted uses <archivo>.key
        if not key:
            return
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
        if messagebox.askyesno("Delete Encrypted File", f"Do you want to delete the encrypted file '{encrypted_file_path}'?"):
            os.remove(encrypted_file_path)
            messagebox.showinfo("Success", f"Encrypted file '{encrypted_file_path}' deleted.")
            
    except Exception as e:
        handle_error(e, "An error occurred during decryption. Ensure the file extension is '.encrypted'.")
    
    
