import random
import logging
import time

import pytest

logging.basicConfig(level=logging.DEBUG)


class DataCorruption():

    def __init__(self):
        logging.info("This is come from DataCorruption ")


if __name__ == "__main__":
    DataCorruption()
