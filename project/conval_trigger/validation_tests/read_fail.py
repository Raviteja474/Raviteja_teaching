import random
import logging
import time

logging.basicConfig(level=logging.DEBUG)


class ReadFail():

    def __init__(self):
        logging.info("This is come from ReadFail")


if __name__ == "__main__":
    ReadFail()