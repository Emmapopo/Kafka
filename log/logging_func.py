import logging

#Set default config
logging.root.setLevel(logging.NOTSET)

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handler
c_handler = logging.StreamHandler()  # where c_handler is console handler
c_handler.setLevel(logging.INFO)

# Create formatters and add it to handler
c_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

#Add handler to the logger
logger.addHandler(c_handler)
