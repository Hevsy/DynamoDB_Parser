import logging

from func import time_now, timestamp

class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno <= logging.INFO

def setup_logging():
    """
    Configures the logging system with error and success handlers.

    This function sets up the logging system to log error messages and successfully parsed lines to separate log files.

    Error messages are logged to a file named 'import-error.{timestamp}.log', and successfully parsed lines are logged to 'import-complete.{timestamp}.log'.

    Both log files are opened in append mode ('a'), and log entries are formatted to include the timestamp and message.
    """

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set logger's level to DEBUG

    # Create a formatter
    formatter = logging.Formatter(f"{timestamp()} | %(message)s")

    # Create a file handler for error logs
    error_handler = logging.FileHandler(
        f"import-error.{time_now('%Y%m%d')}.{time_now('%H%M%S')}.{time_now('%Z')}.log",
        mode="a",
    )
    error_handler.setFormatter(formatter)
    error_handler.setLevel(logging.ERROR)  # Set error handler's level to ERROR
    logger.addHandler(error_handler)

    # Create a file handler for successful logs
    success_handler = logging.FileHandler(
        f"import-complete.{time_now('%Y%m%d')}.{time_now('%H%M%S')}.{time_now('%Z')}.log",
        mode="a",
    )
    success_handler.setLevel(logging.INFO)  # Set success handler's level to INFO
    success_handler.setFormatter(formatter)
    success_handler.addFilter(logging.Filter(logging.INFO))  # Filter out levels higher than INFO
    logger.addHandler(success_handler)

