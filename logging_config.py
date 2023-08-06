import logging

from func import time_now, timestamp


def setup_logging():
    """
    Configures the logging system with error and success handlers.

    This function sets up the logging system to log error messages and successfully parsed lines to separate log files.

    Error messages are logged to a file named 'import-error.{timestamp}.log', and successfully parsed lines are logged to 'import-complete.{timestamp}.log'.

    Both log files are opened in append mode ('a'), and log entries are formatted to include the timestamp and message.
    """

    # logging.basicConfig(level=logging.INFO, format="%(message)s")

    error_handler = logging.FileHandler(
        f"import-error.{time_now('%Y%m%d')}.{time_now('%H%M%S')}.{time_now('%Z')}.log",
        mode="a",
    )
    error_handler.setLevel(logging.ERROR)

    success_handler = logging.FileHandler(
        f"import-complete.{time_now('%Y%m%d')}.{time_now('%H%M%S')}.{time_now('%Z')}.log",
        mode="a",
    )
    success_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(f"{timestamp()} %(message)s")
    error_handler.setFormatter(formatter)
    success_handler.setFormatter(formatter)

    logging.getLogger().addHandler(error_handler)
    logging.getLogger().addHandler(success_handler)
