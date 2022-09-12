import logging
import sys


def create_logger(loglevel: str) -> None:
    logging.basicConfig(
        format="%(asctime)s - %(message)s",
        level=loglevel,
        stream=sys.stdout,
    )
