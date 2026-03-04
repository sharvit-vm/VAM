import logging

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("smart_processor")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        # File handler to put logs in app.log file
        file_handler = logging.FileHandler("app.log")
        file_handler.setLevel(logging.INFO)

        # Console handler to put logs in console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    logger.propagate = False
    return logger
logger = setup_logger()