import logging

# Configure logging
import os

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',filemode='w')

# Log some messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
logging.shutdown()
