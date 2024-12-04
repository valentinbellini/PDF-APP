from src.gui.tk_window_pdf_pass import *
from src.gui.tk_window_encrypt import *
from src.gui.tk_window_pdf_metadata import *
import webbrowser
from logging_config import configure_logging
import logging

# Function to open github repo link in web browser
def open_link(event):
    webbrowser.open("https://github.com/valentinbellini/PDF-APP")
    
# Configurar logging
configure_logging()
logging.info("App Init")

    
# Create main window
root = tk.Tk()
root.title("Also PDF V1.1")
root.geometry("300x250")

# Create main buttons
tk.Button(root, text="PDF Password", command=open_pdf_lock, width=20, height=2).pack(pady=10)
tk.Button(root, text="File Encrypt", command=open_encrypt_file, width=20, height=2).pack(pady=10)
tk.Button(root, text="PDF Metadata", command=open_pdf_metadata, width=20, height=2).pack(pady=10)


# Create label to show up the link text
link = tk.Label(root, text="https://github.com/valentinbellini/PDF-APP", fg="blue", cursor="hand2")
link.pack(pady=20)

# Associate the mouse click with the function to open the link
link.bind("<Button-1>", open_link)

# App main bucle init
root.mainloop()