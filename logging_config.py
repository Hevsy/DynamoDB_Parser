import logging

from func import time_now, timestamp


def setup_logging():

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    error_handler = logging.FileHandler(
        f"import-error.{time_now('%Y%m%d')}.{time_now('%H%M%S')}.{time_now('%Z')}.log",
        mode="a",
    )
    error_handler.setLevel(logging.ERROR)

    success_handler = logging.FileHandler(f"import-complete.{time_now('%Y%m%d')}.{time_now('%H%M%S')}.{time_now('%Z')}.log", mode="a")
    success_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(f"{timestamp()} %(message)s")
    error_handler.setFormatter(formatter)
    success_handler.setFormatter(formatter)

    logging.getLogger().addHandler(error_handler)
    logging.getLogger().addHandler(success_handler)
