import logging

def get_logger(name):
    """
    Creates and configures a logger with the given name.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():  # Avoid duplicate handlers
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.ERROR)
    return logger

def handle_error(exception, user_message):
    """
    Handles errors centrally by logging and displaying messages.

    Parameters:
        exception (Exception): The exception object to log.
        user_message (str): The message to show to the user in the UI.
    """
    logger = logging.getLogger(__name__)  # Still log in utils
    logger.error(f"{exception.__class__.__name__}: {exception}")
