import logging

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log", mode="a"),  # Guardar en archivo
            logging.StreamHandler(),  # Mostrar en consola
        ],
    )
