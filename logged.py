# import logging
# from datetime import datetime

# # Create a log filename with timestamp (optional)
# log_filename = f"logs/streamlit_log_{datetime.now().strftime('%Y-%m-%d')}.log"

# # Create a logs folder if it doesn't exist
# import os
# os.makedirs("logs", exist_ok=True)

# # Configure logging
# logging.basicConfig(
#     level=logging.ERROR,  # Log only errors (use DEBUG or INFO for more verbosity)
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename=log_filename,
#     filemode='a'  # Append mode
# )

# import logging
# from logging.handlers import RotatingFileHandler
# # Configure logging
# logging.basicConfig(
#     filename='app.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# # Example to log when logging is initialized
# logging.info("Logging is configured.")


# # Configure rotating file handler
# handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=3)
# logging.basicConfig(
#     handlers=[handler],
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# logging.info('This is a log message.')


# logged.py
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, 'app.log')

    # Create rotating file handler
    handler = RotatingFileHandler(log_path, maxBytes=10000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger("streamlit_logger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(handler)
        logger.info("✅ Logger initialized successfully.")  # <-- Default message

    return logger
