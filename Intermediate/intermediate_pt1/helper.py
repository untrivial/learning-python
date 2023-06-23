import logging
logger = logging.getLogger(__name__)
logger.info("Hello from helper")
# logger.propagate = False
  # stops the main.py from logging (stops propagating to the base logger)